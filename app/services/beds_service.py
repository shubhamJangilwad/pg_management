from fastapi import HTTPException
from app.models.beds import Bed
from app.models.rooms import Room
from app.models.room_pricing import RoomPricing
from app.models.buildings import Building
from sqlalchemy import and_




def create_bed_service(body, current_user, db):

    room = db.query(Room
                    ).join(
                        Building,Room.building_id == Building.id
                        ).filter(
                            Room.id == body.room_id,
                            Building.owner_id == current_user.id).first()

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found or you do not have access to this room"
        )

    bed_count = db.query(Bed).filter(Bed.room_id == room.id).count()

    bed_exists = db.query(Bed).filter(Bed.room_id == room.id,Bed.bed_number == body.bed_number).first()

    pricing = db.query(RoomPricing).filter(
            RoomPricing.owner_id == current_user.id,
            RoomPricing.sharing_type == room.sharing_type
        ).first()

    if bed_count >= room.sharing_type:
        raise HTTPException(
            status_code= 409,
            detail="can not create bed it's reched its limit"
        )

    if bed_exists:
        raise HTTPException(
            status_code=409,
            detail= "Bed already exists"
        )

    if not pricing:
        raise HTTPException(
            status_code=404,
            detail="Pricing not found for this sharing type"
        )

    else: 
        try:
            bed = Bed(
                room_id = body.room_id,
                bed_number = body.bed_number
            )

            db.add(bed)
            db.commit()
            db.refresh(bed)

            return {
        "id": bed.id,
        "room_id": bed.room_id,
        "bed_number": bed.bed_number,
        "monthly_rent": pricing.monthly_rent,
        "deposite": pricing.deposite,
        "status": bed.status
    }

        except Exception as e:
            db.rollback()
            print(e)


def get_beds_service(current_user,db):
    beds = db.query(Bed,
                    RoomPricing.monthly_rent,
                    RoomPricing.deposite
                    ).join(
                        Room,
                        Bed.room_id == Room.id
                        ).join(
                            Building,
                            Room.building_id == Building.id
                            ).join(
                                 RoomPricing,
                                 and_(
                                     RoomPricing.owner_id == Building.owner_id,
                                     RoomPricing.sharing_type == Room.sharing_type
                                      )
                            ).filter(
                            Building.owner_id == current_user.id
                        ).all()

    if not beds:
        raise HTTPException(
            status_code=404,
            detail="beds not found"
        )

    else:
        result = []

        for bed, monthly_rent, deposite in beds:
            result.append({
                "id": bed.id,
                "room_id": bed.room_id,
                "bed_number": bed.bed_number,
                "monthly_rent": monthly_rent,
                "deposite": deposite,
                "status": bed.status
            })

    return result


def get_room_beds_service(building_id,
        room_id,
        current_user,
        db):
    get_bui_room_b = db.query(Bed.id,
    Bed.room_id,
    Bed.bed_number,
    RoomPricing.monthly_rent,
    RoomPricing.deposite,
    Bed.status,
    Building.id.label("building_id"),
    Building.building_name
                    ).join(
                        Room, Bed.room_id == Room.id
                        ).join(
                            Building,
                            Room.building_id == Building.id
                            ).join(
                                RoomPricing,
                                and_(
                                    RoomPricing.owner_id == Building.owner_id,
                                    RoomPricing.sharing_type == Room.sharing_type   
                                )
                                ).filter(
                                    Bed.room_id == room_id,
                                    Room.building_id == building_id,
                                    Building.owner_id == current_user.id
                                    ).all()

    if not get_bui_room_b:
        raise HTTPException(
            status_code=404,
            detail="No Bed Found"
        )

    else:
       result = []

       for bed_id, db_room_id, bed_number, monthly_rent, deposite, status, db_building_id, building_name in get_bui_room_b:
           result.append({
               "id" : bed_id,
               "room_id" : db_room_id,
               "bed_number" : bed_number,
               "monthly_rent" : monthly_rent,
               "deposite" : deposite,
               "status" : status,
               "building_id" :db_building_id,
               "building_name" : building_name
           })

    return result