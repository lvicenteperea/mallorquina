import mysql.connector
import pyodbc

from config.config import MYSQL_CONFIG

def obtener_configuracion_mysql():
    return mysql.connector.connect(**MYSQL_CONFIG)

def obtener_conexion_sqlserver(conexion_json):
    return pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={conexion_json['host']};"
        f"DATABASE={conexion_json['database']};UID={conexion_json['user']};PWD={conexion_json['password']}"
    )
