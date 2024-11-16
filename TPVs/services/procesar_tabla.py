from models.mll_tablas import obtener_campos_tabla, crear_tabla_destino
from models.mll_cfg_bbdd import obtener_conexion_sqlserver

def procesar_tabla(tabla, conn_mysql):
    # Obtener configuración y campos necesarios
    cursor_mysql = conn_mysql.cursor(dictionary=True)
    
    # Obtener nombre de la tabla y si se debe borrar
    cursor_mysql.execute("SELECT * FROM mll_tablas WHERE ID = %s", (tabla["ID_Tabla"],))
    tabla_config = cursor_mysql.fetchone()
    nombre_tabla = tabla_config["Nombre_Tabla"]
    borrar_tabla = tabla_config["Borrar_Tabla"]

    # Obtener campos de la tabla
    campos = obtener_campos_tabla(tabla["ID_Tabla"])
    
    # Borrar tabla si corresponde
    if borrar_tabla:
        cursor_mysql.execute(f"DROP TABLE IF EXISTS {nombre_tabla}")
        conn_mysql.commit()

    # Crear tabla si no existe
    crear_tabla_destino(nombre_tabla, campos, conn_mysql)

    # Conectar a la base de datos SQL Server
    bbdd_config = obtener_conexion_sqlserver(tabla["ID_BBDD"])
    conn_sqlserver = obtener_conexion_sqlserver(bbdd_config)

    try:
        # Leer datos desde SQL Server
        cursor_sqlserver = conn_sqlserver.cursor()
        select_query = f"SELECT {', '.join([campo['Campo_Nombre'] for campo in campos])} FROM {nombre_tabla}"
        cursor_sqlserver.execute(select_query)
        registros = cursor_sqlserver.fetchall()

        # Preparar e insertar los registros en BD_Mallorquina
        cursor_mysql = conn_mysql.cursor()
        columnas_mysql = [campo["Campo_Nombre"] for campo in campos] + ["Origen_BBDD"]
        insert_query = f"""
            INSERT INTO {nombre_tabla} ({', '.join(columnas_mysql)})
            VALUES ({', '.join(['%s'] * len(columnas_mysql))})
        """
        for registro in registros:
            registro_destino = list(registro) + [tabla["ID_BBDD"]]  # Añadimos el origen
            cursor_mysql.execute(insert_query, registro_destino)
        conn_mysql.commit()
    finally:
        conn_sqlserver.close()
