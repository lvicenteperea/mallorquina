import os

# Configuración general
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "tu_api_key")
MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Admin",
    "database": "mallorquina"
}
