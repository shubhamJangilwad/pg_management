from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from app.schemas.bed_schema import BedCreate , BedResponse
from app.database import get_db
from app.services.auth import get_current_user
from app.services.beds_service import create_bed_service




Beds = APIRouter() 

@Beds.post("/create/bed",response_model=BedResponse)
def create_bed(body : BedCreate,
               current_user = Depends(get_current_user),
               db : Session = Depends(get_db)):
        return create_bed_service(body,current_user,db)