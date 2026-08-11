from app.database import Base   
from sqlalchemy import Column, Integer , String , DateTime , Boolean
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(150), unique= True, nullable=False, index=True)
    phone_no = Column(String(15), unique=True , nullable= False)
    password = Column(String(500), nullable=False)
    role= Column(String(100),nullable=False)
    is_active = Column(Boolean , default=True)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_default=func.now(), onupdate=func.now())


