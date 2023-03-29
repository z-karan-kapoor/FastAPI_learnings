from fastapi import APIRouter,Depends,HTTPException,status
from src.models.database import get_db,engine
from src.services.hashing import Hasher
from src.schemas.schemas import ShowUser, UserCreate
from src.models.all import User
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/user/{id}', tags=["user"])
def get_user(id:int,db: Session=Depends(get_db)):
    db_data = db.query(User).with_entities(User.email,User.is_active).filter(id==User.id)
    if db_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {id} doesn't exists")
    return db_data


@router.post("/users",tags=["user"], response_model=ShowUser)
def create_user(user: UserCreate,db: Session=Depends(get_db)):
    user = User(email=user.email,password=Hasher.get_hash_password(user.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user