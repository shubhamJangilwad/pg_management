from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user_schema import UserCreate , UserResponse , UserLogin ,TokenResponse
from app.services.user_service import user_create_service ,user_login_service
from app.services.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm



User = APIRouter()


@User.post("/user/register", response_model = UserResponse)
def user_register(body : UserCreate , 
                db : Session = Depends(get_db)):
        return user_create_service(body,db)


@User.post("/user/login",response_model=TokenResponse)
def user_login(form_data : OAuth2PasswordRequestForm = Depends(),
               db : Session = Depends(get_db)):
        return user_login_service(form_data,db)


@User.get("/user/profile", response_model=UserResponse)
def user_profile_get(current_user = Depends(get_current_user)):
        return current_user