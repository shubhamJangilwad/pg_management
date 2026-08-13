from app.models.room_pricing import RoomPricing
from fastapi import HTTPException



def create_room_pricing_service(body,current_user,db):
    room_pricing_exist = db.query(RoomPricing).filter(RoomPricing.owner_id == current_user.id ,
                                                      RoomPricing.sharing_type == body.sharing_type).first()

    if room_pricing_exist:
        raise HTTPException(
            status_code= 409,
            detail= "room_pricing data already exist"
        )

    else:
        try:
            room_pricing = RoomPricing(
                owner_id = current_user.id,
                sharing_type = body.sharing_type,
                monthly_rent = body.monthly_rent,
                deposite = body.deposite
            )

            db.add(room_pricing)
            db.commit()
            db.refresh(room_pricing)

            return room_pricing

        except Exception as e:
            db.rollback()
            print(e)