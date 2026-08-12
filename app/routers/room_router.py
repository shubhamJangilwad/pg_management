from fastapi import APIRouter , Depends
from app.database import get_db
from app.schemas.room_schema import RoomCreate
from sqlalchemy.orm import Session
from app.services.auth import get_current_user
from app.services.room_service import create_room_service, get_rooms_service


Rooms = APIRouter()

@Rooms.post("/create/room")
def create_room(body : RoomCreate,
                current_user = Depends(get_current_user),
                db:Session = Depends(get_db)):

    return create_room_service(body,current_user,db)


@Rooms.get("/get/room")
def get_room(current_user = Depends(get_current_user),
             db:Session = Depends(get_db)):

    return get_rooms_service(current_user,db)