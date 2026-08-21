from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app.schemas.payment_schema import PaymentCreate , TenantCheckout , TenantPaymentResponse
from app.database import get_db
from app.services.auth import get_current_user
from app.services.payment_service import create_payment_service , tenant_checkout_service ,get_payments_service

Payments = APIRouter()

@Payments.post("/create/payment")
def create_payment(body : PaymentCreate,
                    current_user = Depends(get_current_user),
                    db : Session = Depends(get_db)):

    return create_payment_service(body,current_user,db)


@Payments.post("/tenant/checkout")
def tenant_checkout(body : TenantCheckout,
                    current_user = Depends(get_current_user),
                    db : Session = Depends(get_db)):

    return tenant_checkout_service(body,current_user,db)


@Payments.get("/get/payments",response_model=List[TenantPaymentResponse])
def get_payments(current_user = Depends(get_current_user),
                 db : Session = Depends(get_db)):
    return get_payments_service(current_user,db)