from datetime import date
from pydantic import EmailStr, BaseModel 

class UserCreate(BaseModel):
    """User attributes input by User"""
    email : EmailStr
    password : str


class ShowUser(BaseModel):
    """Response Model to show neccessary data"""
    email: EmailStr
    is_active: bool
    class Config:
        orm_mode=True

class ItemCreate(BaseModel):
    """Item attributes input by User"""
    title: str
    description: str

class ShowItem(BaseModel):
    title: str
    description: str
    date_posted: date
    class Config:
        orm_mode=True