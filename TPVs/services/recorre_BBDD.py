from datetime import datetime
from config.database import conexion_mysql
from models.mll_cfg import obtener_configuracion_general, actualizar_en_ejecucion
from services.sendgrid_service import enviar_email
from TPVs.services.sync_una_BBDD import procesar_BBDD

def ejecutar_proceso():
    config = obtener_configuracion_general()


    if not config.get("ID", False):
        print("No se han encontrado datos de configuración", config["En_Ejecucion"])
        return
    
    if config["En_Ejecucion"]:
        print("El proceso ya está en ejecución.")
        return

    actualizar_en_ejecucion(1)

    try:
        conn_mysql = conexion_mysql("General")
        cursor_mysql = conn_mysql.cursor(dictionary=True)

        cursor_mysql.execute("SELECT * FROM mll_cfg_bbdd")
        tablas_bbdd = cursor_mysql.fetchall()

        for tabla in tablas_bbdd:
                print("---------------------------------------------------------------------------------------")
                print(f"Procesando TIENDA: {tabla}")
                print("---------------------------------------------------------------------------------------")

                # Aquí va la lógica específica para cada tabla
                procesar_BBDD(tabla, conn_mysql)

                print("sync.07")
                cursor_mysql.execute(
                    "UPDATE mll_cfg_bbdd SET Ultima_fecha_Carga = %s WHERE ID = %s",
                    (datetime.now(), tabla["ID"])
                )
                conn_mysql.commit()

        cursor_mysql.closed()

    except Exception as e:
        print(f"Error durante el proceso: {e}")


    finally:
        conn_mysql.closed()
        actualizar_en_ejecucion(0)
        enviar_email(
            config["Lista_emails"],
            "Proceso finalizado",
            "El proceso de sincronización ha terminado."
        )