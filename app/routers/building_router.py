from fastapi import APIRouter , Depends 
from app.services.auth import get_current_user
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.building_schema import BuildingCreate ,BuildingResponse
from app.services.building_service import create_building_service, get_buildings_service




Buildings = APIRouter()

@Buildings.post("/create/building", response_model=BuildingResponse)
def create_building(body : BuildingCreate,
                    current_user = Depends(get_current_user),
                    db : Session = Depends(get_db)):
        return create_building_service(body,db,current_user)

@Buildings.get("/get/buildings")
def get_buildings(current_user = Depends(get_current_user),
                  db : Session = Depends(get_db)):
        return get_buildings_service(db,current_user)