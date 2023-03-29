from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # is_admin = Column(Boolean, default=False)

    items = relationship("Items", back_populates="owner")



class Items(Base):
    __tablename__ = "Items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    date_posted = Column(Date)
    owner_id = Column(Integer, ForeignKey("User.id"))

    owner = relationship("User", back_populates="items")
