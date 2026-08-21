from datetime import date
from pydantic import BaseModel
from typing import Optional , List

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

class RentPaymentResponse(BaseModel):
    payment_month: str
    amount: int
    payment_status: str


class RefundResponse(BaseModel):
    payment_month: str
    maintenance_charge: int 
    refund_amount: int
    payment_status: str


class TenantPaymentResponse(BaseModel):
    tenant_id: int
    rent_payments: List[RentPaymentResponse] 
    refund: Optional[RefundResponse] = None

    model_config = {
        "from_attributes" : True
    }