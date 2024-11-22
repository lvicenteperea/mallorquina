from datetime import datetime, timedelta
from config.database import conexion_mysql
from models.mll_cfg import obtener_configuracion_general, actualizar_en_ejecucion
from services.sendgrid_service import enviar_email
from services.procesar_tabla import procesar_tabla

def ejecutar_proceso():
    config = obtener_configuracion_general()
    print(config)

    if not config.get("En_Ejecucion"):
        print("No se han encontrado datos de configuración")
        return
    
    if config["En_Ejecucion"]:
        print("El proceso ya está en ejecución.")
        return

    actualizar_en_ejecucion(1)

    try:
        conn_mysql = conexion_mysql("General")
        cursor_mysql = conn_mysql.cursor(dictionary=True)

        cursor_mysql.execute("SELECT * FROM mll_tablas_bbdd")
        tablas_bbdd = cursor_mysql.fetchall()

        for tabla in tablas_bbdd:
            ultima_actualizacion = tabla["Fecha_Ultima_Actualizacion"]
            intervalo = tabla["Cada_Cuanto_Ejecutar"]

            if datetime.now() > ultima_actualizacion + timedelta(days=intervalo):
                # print(f"Procesando tabla: {tabla['ID_Tabla']}")
                print(f"Procesando tabla: {tabla}")

                # Aquí va la lógica específica para cada tabla
                procesar_tabla(tabla, conn_mysql)

                print("sync.07")
                cursor_mysql.execute(
                    "UPDATE mll_tablas_bbdd SET Fecha_Ultima_Actualizacion = %s WHERE ID = %s",
                    (datetime.now(), tabla["ID"])
                )
                conn_mysql.commit()

    except Exception as e:
        print(f"Error durante el proceso: {e}")
    finally:
        actualizar_en_ejecucion(0)
        enviar_email(
            config["Lista_emails"],
            "Proceso finalizado",
            "El proceso de sincronización ha terminado."
        )
