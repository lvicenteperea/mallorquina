from datetime import datetime, timedelta
from services.procesar_tabla import procesar_tabla

'''
ejecutar_proceso: Sincroniza todas las tablas de una tienda. Recibe un json con los datos del registro de mll_cfg_bbdd:
  - ID int: Es el ID de la tabla que vamos a tratar
  - Nombre str: Es el nombre de la tienda
  - Conexion str: es la conexión de la tienda en formato -->{"host": "ip", "port": "1433", "user": "usuario", "database": "nombre_database", "p a s  s w o  r d": "la_contraseña"}
  - Ultima_Fecha_Carga str: fecha en la que se sincronizó la última vez
'''
def procesar_BBDD(reg_cfg_bbdd, conn_mysql):
    try:
        # conn_mysql = conexion_mysql("General")
        cursor_mysql = conn_mysql.cursor(dictionary=True)

        cursor_mysql.execute("SELECT * FROM mll_tablas_bbdd where id_bbdd = %s", (reg_cfg_bbdd["ID"],))
        tablas_bbdd = cursor_mysql.fetchall()

        for tabla in tablas_bbdd:
            ultima_actualizacion = tabla["Fecha_Ultima_Actualizacion"]
            intervalo = tabla["Cada_Cuanto_Ejecutar"]

            if (intervalo == 0 or (datetime.now() > ultima_actualizacion + timedelta(days=intervalo))):
                # print(f"Procesando tabla: {tabla['ID_Tabla']}")
                print("---------------------------------------------------------------------------------------")
                print(f"Procesando tabla: {tabla}")
                print("---------------------------------------------------------------------------------------")

                # Aquí va la lógica específica para cada tabla
                procesar_tabla(tabla, conn_mysql)

                cursor_mysql.execute(
                    "UPDATE mll_tablas_bbdd SET Fecha_Ultima_Actualizacion = %s WHERE ID = %s",
                    (datetime.now(), tabla["ID"])
                )
                conn_mysql.commit()
        
    except Exception as e:
        print("")
        print("---------------------------")
        print(f"ERROR durante el proceso: {e}")
        print("---------------------------")
        print("")
        
    finally:
        cursor_mysql.close()

