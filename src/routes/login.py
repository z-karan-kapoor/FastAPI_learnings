from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from src.models.database import get_db
from src.models.all import User
from src.services.hashing import Hasher
from sqlalchemy.orm import Session
from jose import jwt
from src.configs.meta_data import MetaData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/token")

router = APIRouter()

@router.post("/login/token")
def retrieve_token_for_authenticated_user(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username"
        )
    if not Hasher.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Password"
        )
    data = {"sub": form_data.username}
    jwt_token = jwt.encode(data, MetaData.settings['SECRET_KEY'], algorithm=MetaData.settings['ALGORITHM'])
    response.set_cookie(key="access_token", value=f"Bearer {jwt_token}", httponly=True)
    return {"access_token": jwt_token, "token_type": "bearer"}