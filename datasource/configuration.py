import os
from .secrets import get_secret

name_db=os.getenv("appdb")
user_db=get_secret("db-user")
password_db=get_secret("db-password")
ip_db=os.getenv("localhost")
port_db=os.getenv("3306")

class Config:
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{user_db}:{password_db}@{ip_db}:{port_db}/{name_db}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False