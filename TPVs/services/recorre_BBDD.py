from datetime import datetime
from config.database import conexion_mysql
from models.mll_cfg import obtener_configuracion_general, actualizar_en_ejecucion
from services.sendgrid_service import enviar_email
from services.sync_una_BBDD import procesar_BBDD

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
        lista_bbdd = cursor_mysql.fetchall()

        for bbdd in lista_bbdd:
                print("")
                print("---------------------------------------------------------------------------------------")
                print(f"Procesando TIENDA: {bbdd}")
                print("---------------------------------------------------------------------------------------")
                print("")

                # Aquí va la lógica específica para cada bbdd
                procesar_BBDD(bbdd, conn_mysql)

                cursor_mysql.execute(
                    "UPDATE mll_cfg_bbdd SET Ultima_fecha_Carga = %s WHERE ID = %s",
                    (datetime.now(), bbdd["ID"])
                )
                conn_mysql.commit()

    except Exception as e:
        print("")
        print("---------------------------")
        print(f"ERROR durante el proceso: {e}")
        print("---------------------------")
        print("")
        

    finally:
        conn_mysql.close()
        actualizar_en_ejecucion(0)
        enviar_email(
            config["Lista_emails"],
            "Proceso finalizado",
            "El proceso de sincronización ha terminado."
        )