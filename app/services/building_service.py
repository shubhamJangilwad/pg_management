from app.models.buildings import Building
from fastapi import HTTPException



def create_building_service(body,db,current_user):
    building_existance = db.query(Building).filter(
        Building.owner_id == current_user.id,
        Building.building_name == body.building_name).first()

    if building_existance:
        raise HTTPException(
            status_code= 409 ,
            detail= "building already exist"
        )

    else:
        try:
            building_create = Building(
                building_name = body.building_name,
                address = body.address,
                city = body.city,
                total_floors = body.total_floors,
                owner_id = current_user.id
            )

            db.add(building_create)
            db.commit()
            db.refresh(building_create)

            return building_create
        except Exception as e:
            db.rollback()
            print(e)

def get_buildings_service(db,current_user):
    user = db.query(Building).filter(Building.owner_id == current_user.id).all()

    if not user:
        raise HTTPException(
            status_code= 402,
            detail= "user not found"
        )

    else:
        return user
