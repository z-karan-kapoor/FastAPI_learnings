from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from src.models.database import get_db
from src.schemas.schemas import ItemCreate, ShowItem
from src. models.all import Items
from sqlalchemy.orm import Session
from typing import List
from fastapi.encoders import jsonable_encoder
from src.routes.login import oauth2_scheme
from jose import jwt
from src.configs.meta_data import MetaData
from src.models.all import User

router = APIRouter()

def get_user_from_token(db, token):
    try:
        payload = jwt.decode(token, MetaData.settings["SECRET_KEY"], MetaData.settings["ALGORITHM"])
        username = payload.get("sub")
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate Credentials",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate Credetials",
        )
    user = db.query(User).filter(User.email == username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return user

@router.post('/item', tags=["items"], response_model=ShowItem)
def create_item(item: ItemCreate,db: Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    user = get_user_from_token(db, token)
    date_posted = datetime.now().date()
    owner_id = user.id
    item = Items(**item.dict(),date_posted=date_posted,owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/item/all", tags=["items"],response_model=List[ShowItem])
def get_all_item(db: Session=Depends(get_db)):
    """Get All Items in the table"""
    items = db.query(Items).all()
    return items

@router.get('/item/{id}', tags=["items"], response_model=ShowItem)
def get_item_by_id(id:int,db: Session=Depends(get_db)):
    """Get Item using ID"""
    db_data = db.query(Items).filter(id==Items.id).first()
    if db_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {id} doesn't exists")
    return db_data

@router.put("/item/update/{id}",tags=["items"])
def update_item_by_id(id:int, item: ItemCreate, db: Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    """Update Item using jsonable_encoder"""
    user = get_user_from_token(db, token)
    existing_item=db.query(Items).filter(Items.id==id)
    if not existing_item.first():
        return {"message":f"No details exists for Item ID: {id}"}
    if existing_item.first().owner_id == user.id:
        existing_item.update(jsonable_encoder(item))
        db.commit()
        return {"message": f"Details successfully updated for Item ID {id}"}
    else:
        return {"message": "You are not authorized"}



@router.put("/item/update1/{id}",tags=["items"])
def update1_item_by_id(id:int, item: ItemCreate, db: Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    """Update Item using __dict__"""
    user = get_user_from_token(db, token)
    existing_item=db.query(Items).filter(Items.id==id)
    if not existing_item.first():
        return {"message":f"No details exists for Item ID: {id}"}
    if existing_item.first().owner_id == user.id:
        existing_item.update(item.__dict__)
        db.commit()
        return {"message": f"Details successfully updated for Item ID {id}"}
    else:
        return {"message": "You are not authorized"}


@router.delete("/item/delete/{id}", tags=["item"])
def delete_item_by_id(id: int, db: Session = Depends(get_db),token:str=Depends(oauth2_scheme)):
    """Delete Item using ID"""
    user = get_user_from_token(db, token)
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No Details found for Item ID {id}"}
    if existing_item.first().owner_id == user.id:
        existing_item.delete()
        db.commit()
        return {"message": f"Item ID {id} has been successfully deleted"}
    else:
        return {"message": "You are not authorized"}
    