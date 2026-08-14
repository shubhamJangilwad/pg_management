from fastapi import FastAPI
from app.database import Base , engine
from app.routers.users_router import User
from app.routers.building_router import Buildings
from app.routers.room_router import Rooms
from app.routers.room_pricing_router import RoomPricing
from app.routers.bed_router import Beds
from app.routers.tenants_router import Tenants

app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(User, tags=["User"])
app.include_router(Buildings , tags=["Buildings"])
app.include_router(Rooms , tags=["Rooms"])
app.include_router(RoomPricing , tags=["RoomPricing"])
app.include_router(Beds , tags=["Beds"])
app.include_router(Tenants, tags=["Tenants"])