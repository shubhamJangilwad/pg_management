from jose import jwt
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
from fastapi import Depends

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
    token : str = Depends(oauth2_scheme)):

    payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )

    return payload
