from config.database import obtener_configuracion_mysql

def obtener_conexion_sqlserver(id_bbdd):
    conn = obtener_configuracion_mysql()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Conexion FROM mll_cfg_bbdd WHERE ID = %s", (id_bbdd,))
    conexion = cursor.fetchone()["Conexion"]
    cursor.close()
    conn.close()
    return conexion
