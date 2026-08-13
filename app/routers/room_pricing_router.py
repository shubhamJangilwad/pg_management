from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from app.schemas.room_pricing_schema import RoomPricingCreate , RoomPricingResponse
from app.database import get_db
from app.services.auth import get_current_user
from app.services.room_pricing_service import create_room_pricing_service




RoomPricing = APIRouter() 

@RoomPricing.post("/create/roomPri", response_model=RoomPricingResponse)
def create_room_pricing(body : RoomPricingCreate,
                        current_user = Depends(get_current_user),
                        db : Session = Depends(get_db)):

    return create_room_pricing_service(body,current_user,db)