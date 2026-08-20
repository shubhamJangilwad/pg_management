from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
<<<<<<< Updated upstream
from app.schemas.bed_schema import BedCreate , BedResponse
=======
from app.schemas.bed_schema import BedCreate , BedResponse , BedDetailResponse
>>>>>>> Stashed changes
from app.database import get_db
from app.services.auth import get_current_user
from app.services.beds_service import create_bed_service




Beds = APIRouter() 

@Beds.post("/create/bed",response_model=BedResponse)
def create_bed(body : BedCreate,
               current_user = Depends(get_current_user),
               db : Session = Depends(get_db)):
<<<<<<< Updated upstream
        return create_bed_service(body,current_user,db)
=======
        return create_bed_service(body,current_user,db)


@Beds.get("/get/beds",response_model=list[BedResponse])
def get_beds(
               current_user = Depends(get_current_user),
               db : Session = Depends(get_db)):
        return get_beds_service(current_user,db)

@Beds.get("/building/{building_id}/room/{room_id}/beds",
    response_model=list[BedDetailResponse]
)
def get_room_beds(
    building_id: int,
    room_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_room_beds_service(
        building_id,
        room_id,
        current_user,
        db
    )
>>>>>>> Stashed changes
