from .base_config import Base_Config

class Prod_Config(Base_Config):
    DEVELOPMENT = False
    DEBUG = True