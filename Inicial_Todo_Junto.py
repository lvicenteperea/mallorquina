import mysql.connector
import pyodbc
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime, timedelta

def obtener_configuracion_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_password",
        database="BD_Mallorquina"
    )

def obtener_conexion_sqlserver(conexion_json):
    return pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={conexion_json['host']};"
        f"DATABASE={conexion_json['database']};UID={conexion_json['user']};PWD={conexion_json['password']}"
    )

def enviar_email(api_key, lista_emails, asunto, contenido):
    message = Mail(
        from_email="notificaciones@tuempresa.com",
        to_emails=lista_emails.split(','),
        subject=asunto,
        html_content=contenido
    )
    sg = SendGridAPIClient(api_key)
    sg.send(message)

def ejecutar_proceso():
    conn_mysql = obtener_configuracion_mysql()
    cursor_mysql = conn_mysql.cursor(dictionary=True)

    # Verificar si ya está en ejecución
    cursor_mysql.execute("SELECT En_Ejecucion FROM mll_cfg LIMIT 1")
    en_ejecucion = cursor_mysql.fetchone()["En_Ejecucion"]
    if en_ejecucion:
        print("El proceso ya está en ejecución.")
        return

    # Marcar como en ejecución
    cursor_mysql.execute("UPDATE mll_cfg SET En_Ejecucion = 1")
    conn_mysql.commit()

    try:
        # Leer tablas a procesar
        cursor_mysql.execute("SELECT * FROM mll_tablas_bbdd")
        tablas_bbdd = cursor_mysql.fetchall()

        for tabla in tablas_bbdd:
            # Validar la fecha de ejecución
            ultima_actualizacion = tabla["Fecha_Ultima_Actualizacion"]
            intervalo = tabla["Cada_Cuanto_Ejecutar"]
            if datetime.now() > ultima_actualizacion + timedelta(days=intervalo):
                # Procesar tabla
                print(f"Procesando tabla: {tabla['ID_Tabla']}")

                # Aquí va el resto de la lógica (crear tabla, insertar registros, etc.)

                # Actualizar última ejecución
                cursor_mysql.execute(
                    "UPDATE mll_tablas_bbdd SET Fecha_Ultima_Actualizacion = %s WHERE ID = %s",
                    (datetime.now(), tabla["ID"])
                )
                conn_mysql.commit()

    except Exception as e:
        print(f"Error durante el proceso: {e}")
    finally:
        # Marcar como no en ejecución
        cursor_mysql.execute("UPDATE mll_cfg SET En_Ejecucion = 0")
        conn_mysql.commit()
        cursor_mysql.close()
        conn_mysql.close()

        # Enviar email
        cursor_mysql.execute("SELECT Lista_emails, Sendgrid_API_Key FROM mll_cfg LIMIT 1")
        cfg = cursor_mysql.fetchone()
        enviar_email(cfg["Sendgrid_API_Key"], cfg["Lista_emails"], "Proceso finalizado", "El proceso de sincronización ha terminado.")

if __name__ == "__main__":
    ejecutar_proceso()
