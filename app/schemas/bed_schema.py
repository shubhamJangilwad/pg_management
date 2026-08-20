from pydantic import BaseModel


class BedCreate(BaseModel):
    room_id : int
    bed_number : str


class BedResponse(BedCreate,BaseModel):
    id : int
    bed_number : str
    monthly_rent : int
    deposite : int
    status : str

<<<<<<< Updated upstream
=======
class BedDetailResponse(BaseModel):
    id: int
    room_id: int
    bed_number: str
    monthly_rent: int
    deposite: int
    status: str
    building_id: int
    building_name: str

>>>>>>> Stashed changes
    model_config = {
        "from_attributes" : True
    }