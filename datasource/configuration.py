import os
from .secrets import get_secret

name_db = os.getenv("NAME_DB", "appdb")
user_db = get_secret("db-user")
password_db = get_secret("db-password")
ip_db = os.getenv("IP_DB", "localhost")
port_db = os.getenv("PORT_DB", "3306")

print(f"→ IP_DB={ip_db}, PORT_DB={port_db}, NAME_DB={name_db}")  # Línea clave para debug

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user_db}:{password_db}@{ip_db}:{port_db}/{name_db}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False