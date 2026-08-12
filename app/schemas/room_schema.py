from pydantic import BaseModel

class RoomCreate(BaseModel):
    building_id : int
    room_number : int
    floor_number : str
    sharing_type : int


    model_config = {
        "from_attributes" : True
    }