from config.database import obtener_configuracion_mysql

def obtener_configuracion_general():
    conn = obtener_configuracion_mysql()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM mll_cfg LIMIT 1")
    config = cursor.fetchone()
    cursor.close()
    conn.close()
    return config

def actualizar_en_ejecucion(estado):
    conn = obtener_configuracion_mysql()
    cursor = conn.cursor()
    cursor.execute("UPDATE mll_cfg SET En_Ejecucion = %s", (estado,))
    conn.commit()
    cursor.close()
    conn.close()
