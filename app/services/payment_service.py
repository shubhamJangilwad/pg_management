from app.models.payments import Payment
from app.models.tenants import Tenant
from app.models.beds import Bed
from app.models.rooms import Room
from app.models.room_pricing import RoomPricing
from app.models.buildings import Building
from fastapi import HTTPException


def create_payment_service(body,current_user,db):
    tenant = db.query(Tenant).join(
        Bed,
        Tenant.bed_id == Bed.id
        ).join(
            Room,
            Bed.room_id == Room.id
            ).join(
                Building,
                Room.building_id == Building.id
                ).filter(
                    Tenant.id == body.tenant_id,
                    Building.owner_id == current_user.id).first()

    if not tenant:
        raise HTTPException(
            status_code=404,
            detail="Tenant not found"
        )

    else:
        try: 
            payment = Payment(
                tenant_id  = tenant.id,
                payment_month = body.payment_month,
                amount = body.amount,
                payment_date = body.payment_date,
                payment_status = "Paid",
                refund_amount = None,
                maintenance_charge = None
                  )
            db.add(payment)
            db.commit()
            db.refresh(payment)

            return payment

        except Exception as e:
            db.rollback()
            print(e)



def tenant_checkout_service(body,current_user,db):
    tenant = db.query(Tenant).join(
            Bed,
            Tenant.bed_id == Bed.id
            ).join(
                Room,
                Bed.room_id == Room.id
                ).join(
                    Building,
                    Room.building_id == Building.id
                    ).filter(
                        Tenant.id == body.tenant_id,
                        Building.owner_id == current_user.id).first()

    maintenance_charge = 1000
    refund_amount = tenant.deposit_paid - maintenance_charge
    
    if not tenant:
        raise HTTPException(
            status_code=404,
            detail="Tenant not found"
        )

    if not tenant.is_active :
        raise HTTPException(
            status_code= 409,
            detail= "tenant is not active/found"
        )

    else: 
        try:
            payment = Payment(
        tenant_id=tenant.id,
        payment_month=body.leave_date.strftime("%B"),
        amount=0,
        payment_date=body.leave_date,
        payment_status="REFUNDED",
        refund_amount=refund_amount,
        maintenance_charge=maintenance_charge
        )

            tenant.leave_date = body.leave_date
            tenant.is_active = False

            bed = db.query(Bed).filter(Bed.id == tenant.bed_id).first()

            bed.status = "VACANT"

            db.add(payment)
            db.commit()
            db.refresh(payment)
            return payment
        
        except Exception as e:
            db.rollback()
            print(e)


def get_payments_service(current_user,db):
    payments = db.query(Payment).join(
        Tenant,
        Payment.tenant_id == Tenant.id
    ).join(
        Bed,
        Tenant.bed_id == Bed.id
    ).join(
        Room,
        Bed.room_id == Room.id
    ).join(
        Building,
        Room.building_id == Building.id
    ).filter(
        Building.owner_id == current_user.id).all()

    if not payments:
        raise HTTPException(
            status_code= 404,
            detail= "Payments Not Found"
        )

    result = {}
    for payment in payments:
        if payment.tenant_id not in result:
            result[payment.tenant_id] = {
                "tenant_id": payment.tenant_id,
                "rent_payments": [],
                "refund": None
            }

        if payment.payment_status == "REFUNDED":
            result[payment.tenant_id]["refund"] = {
                "payment_month": payment.payment_month,
                "maintenance_charge": payment.maintenance_charge,
                "refund_amount": payment.refund_amount,
                "payment_status": payment.payment_status
            }

        else:
            result[payment.tenant_id]["rent_payments"].append({
                "payment_month": payment.payment_month,
                "amount": payment.amount,
                "payment_status": payment.payment_status
            })


    return list(result.values())