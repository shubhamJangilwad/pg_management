from app.models.rooms import Room
from fastapi import HTTPException
from app.models.buildings import Building



def create_room_service(body,current_uer,db):
    building = db.query(Building).filter(Building.id == body.building_id,
                        Building.owner_id == current_uer.id).first()
                        

    if not building:
        raise HTTPException(
            status_code= 403,
            detail= "you do not have access to this building"
        )

    room_exist = db.query(Room).filter(Room.building_id == body.building_id ,
                                       Room.room_number == body.room_number)

    if room_exist:
        raise HTTPException(
            status_code=409,
            detail="room already exists"
        )
    try:
        room = Room(
            building_id = body.building_id,
            room_number = body.room_number,
            floor_number = body.floor_number,
            sharing_type = body.sharing_type
            )

        db.add(room)
        db.commit()
        db.refresh(room)

        return room

    except Exception as e:
        db.rollback()
        print(e)

def get_rooms_service(current_user,db):
    room = db.query(Room).join(Building, 
                               Room.building_id == Building.id).filter(Building.owner_id == current_user.id).all()
    if not room:
        raise HTTPException(
        status_code=404,
        detail="No rooms found"
    )

    return room

