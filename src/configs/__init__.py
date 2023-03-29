import os
from dotenv import load_dotenv
from .dev_config import Dev_Config
from .prod_config import Prod_Config
ROOT_DIR=os.path.join(os.path.dirname(__file__),"../..")
DOT_ENV_PATH=os.path.join(ROOT_DIR,".env")
load_dotenv(DOT_ENV_PATH)

config={"dev": Dev_Config, "prod": Prod_Config}

def init_app(app):
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(config[app_settings])
    return app