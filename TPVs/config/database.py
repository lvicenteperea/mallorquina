import mysql.connector
import pyodbc

from config.config import MYSQL_CONFIG

def conexion_mysql():
    print('DB.Config.01', MYSQL_CONFIG)
    return mysql.connector.connect(**MYSQL_CONFIG)

def conexion_sqlserver(conexion_json):
    print("con_sqlserver.01", f"DRIVER={{SQL Server}};SERVER={conexion_json['host']};"
        f"DATABASE={conexion_json['database']};UID={conexion_json['user']};PWD={conexion_json['password']}")

    return pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={conexion_json['host']};"
        f"DATABASE={conexion_json['database']};UID={conexion_json['user']};PWD={conexion_json['password']}"
    )
