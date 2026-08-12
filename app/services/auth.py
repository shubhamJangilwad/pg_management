from jose import jwt
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
from fastapi import Depends ,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import User

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

def create_access_token(data: dict):
    to_encode = data.copy()

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def verify_access_token(token : str):    
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload

def get_current_user(
    token : str = Depends(oauth2_scheme),
    db : Session = Depends(get_db) 
    ):
    payload = verify_access_token(token)

    user_id = payload.get("user_id")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code= 401,
            detail= "User not found"
        )

    if not user.is_active:
        raise HTTPException(
            status_code= 403,
            detail="user account is inactive"
        )

    return user


