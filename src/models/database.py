import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.configs.base_config import Base_Config


SQLALCHEMY_DATABASE_URL = Base_Config.getDBConnectionString()


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
connection=engine.connect()
Base = declarative_base()


def get_db() -> Generator:
    """ For Dependency Injection """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()