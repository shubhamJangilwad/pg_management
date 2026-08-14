from pydantic import BaseModel
from datetime import date



class TenantCreate(BaseModel):
    bed_id : int
    full_name : str
    phone_number : str
    aadhar_number : str
    join_date : date


class TenantResponse(TenantCreate,BaseModel):
    id : int
    leave_date: date | None
    deposit_paid: int
    is_active: bool

    model_config = {
        "from_attributes" : True
    }