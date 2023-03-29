import os
from dotenv import load_dotenv
from src.configs.base_config import Base_Config

load_dotenv(dotenv_path=".env")

class MetaData:
    settings={
        "TITLE" : "MY APPLICATION",
        "VERSION" :   "0.0.1",
        "DESCRIPTION" : """## This is a FastAPI App""",
        "NAME" : "Karan",
        "EMAIL" : "karankapoor@gmail.com",
        "DATABASE_URL" : Base_Config.SQLALCHEMY_DATABASE_URL,
        "SECRET_KEY" : os.getenv("SECURITY_KEY"),
        "ALGORITHM" : "HS256"
}
