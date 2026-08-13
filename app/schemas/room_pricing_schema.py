from pydantic import BaseModel


class RoomPricingCreate(BaseModel):
    sharing_type : int
    monthly_rent : int
    deposite : int


class RoomPricingResponse(RoomPricingCreate,BaseModel):
    id : int
    owner_id : int

    model_config = {
        "from_attributes" : True
    }