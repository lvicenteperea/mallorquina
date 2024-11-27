from config.database import conexion_mysql

def obtener_configuracion_general():
    conn = conexion_mysql("obtener_configuracion_general")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM mll_cfg LIMIT 1")
    config = cursor.fetchone()
    print(config)
    cursor.close()
    conn.close()
    return config

def actualizar_en_ejecucion(estado):
    conn = conexion_mysql("actualizar_en_ejecucion")
    cursor = conn.cursor()
    cursor.execute("UPDATE mll_cfg SET En_Ejecucion = %s", (estado,))
    conn.commit()
    cursor.close()
    conn.close()
