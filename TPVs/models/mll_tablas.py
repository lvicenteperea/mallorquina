def obtener_campos_tabla(id_tabla):
    conn = obtener_configuracion_mysql()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM mll_campos WHERE ID_Tabla = %s", (id_tabla,))
    campos = cursor.fetchall()
    cursor.close()
    conn.close()
    return campos

def crear_tabla_destino(nombre_tabla, campos, conn_mysql):
    cursor = conn_mysql.cursor()
    columnas = ", ".join([f"{campo['Campo_Nombre']} {campo['Campo_Tipo']}" for campo in campos])
    columnas += ", Origen_BBDD VARCHAR(100)"
    query = f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({columnas})"
    cursor.execute(query)
    conn_mysql.commit()
    cursor.close()
    