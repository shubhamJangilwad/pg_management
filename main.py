from fastapi import FastAPI
from app.database import Base , engine
from app.routers.users_router import User


app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(User, tags=["User_router"])