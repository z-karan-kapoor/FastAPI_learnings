import os
from dotenv import load_dotenv

ROOT_DIR=os.path.join(os.path.dirname(__file__),"../..")
DOT_ENV_PATH=os.path.join(ROOT_DIR,".env")
load_dotenv(DOT_ENV_PATH)

class Base_Config(object):

    def getDBConnectionString():
        config={}
        config["username"]=os.getenv("DB_USERNAME")
        config["host"]=os.getenv("DB_HOST")
        config["password"]=os.getenv("DB_PASSWORD")
        config["database"]=os.getenv("DATABASE")
        config["port"]=os.getenv("DB_PORT")
        con_str= f"mysql+pymysql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
        return con_str

    SQLALCHEMY_DATABASE_URL = getDBConnectionString()


