from pydantic import BaseModel , EmailStr , ConfigDict 
from typing import Optional

class UserCreate(BaseModel):
    full_name : str
    email : EmailStr
    phone_no : str
    password : str


class UserResponse(BaseModel):
    id : int
    full_name : str
    email : EmailStr
    phone_no : str
    role : str
    is_active : bool


class UserLogin(BaseModel):
    email : EmailStr
    password : str



class TokenResponse(BaseModel):
    access_token : str
    token_type : str

    model_config = {
        "from_attributes":True}

