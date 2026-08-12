from pydantic import BaseModel

class BuildingCreate(BaseModel):

    building_name : str
    address : str
    city : str
    total_floors : int

class BuildingResponse(BuildingCreate,BaseModel):
    id : int
    owner_id : int

    model_config = {
        "from_attributes" : True
    }