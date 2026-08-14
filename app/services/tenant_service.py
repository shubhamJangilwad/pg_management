from app.models.tenants import Tenant
from app.models.beds import Bed
from app.models.buildings import Building
from app.models.rooms import Room
from app.models.room_pricing import RoomPricing
from fastapi import HTTPException




def create_tenant_service(body,current_user,db):

    bed = db.query(Bed).join(
        Room,
        Bed.room_id == Room.id
    ).join(
        Building,
        Room.building_id == Building.id
    ).filter(
        Bed.id == body.bed_id,
        Building.owner_id == current_user.id
    ).first()

    if not bed:
        raise HTTPException(
        status_code=404,
        detail="Bed not found or you do not have access to this bed"
    )


    if bed.status != "VACANT":
        raise HTTPException(
        status_code=409,
        detail="Selected bed is already occupied"
    )


    room = db.query(Room).filter(Room.id == bed.room_id).first()

    if not room:
         raise HTTPException(
              status_code= 404,
              detail= "sharing_type not found"

         )
    pricing = db.query(RoomPricing).filter(
                RoomPricing.owner_id == current_user.id,
                RoomPricing.sharing_type == room.sharing_type
            ).first()


    if not pricing:
            raise HTTPException(
                status_code=404,
                detail="Pricing not found for this sharing type"
            )
    

    else:
        try:
            tenant = Tenant(
                bed_id = body.bed_id,
                full_name = body.full_name,
                phone_number = body.phone_number,
                aadhar_number = body.aadhar_number,
                join_date = body.join_date,
                deposit_paid = pricing.deposite
                
            )
            bed.status = "OCCUPIED"

            db.add(tenant)
            db.commit()
            db.refresh(tenant)
            return tenant
        except Exception as e:
            db.rollback()
            raise e

def get_tenants_service(current_user,db):
     tenants = db.query(Bed).join(
             Room,
             Bed.room_id == Room.id
         ).join(
             Building,
             Room.building_id == Building.id
         ).filter(
             Building.owner_id == current_user.id
         ).all()

     if not tenants:
          raise HTTPException(
               status_code= 404,
               detail= "tenants not found"
          )

     else:
          return tenants