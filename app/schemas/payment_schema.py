from datetime import date
from pydantic import BaseModel

class PaymentCreate(BaseModel):
    tenant_id : int
    payment_month : str
    amount : int
    payment_date : date


class PaymentResponse(PaymentCreate,BaseModel):
    id : int
    payment_status : str
    refund_amount : int
    maintenance_charge : int
    is_active : bool
    created_at : date


class TenantCheckout(BaseModel):
    tenant_id : int
    leave_date : date

    model_config = {
        "from_attributes" : True
    }