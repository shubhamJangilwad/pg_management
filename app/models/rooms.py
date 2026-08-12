from app.database import Base
from sqlalchemy import Column , String , Integer , DateTime,ForeignKey , Boolean
from sqlalchemy.sql import func

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer , primary_key= True , index=True)
    building_id = Column(Integer , ForeignKey("pg_building.id"), nullable=False)
    room_number = Column(String(10) , nullable=False)
    floor_number = Column(Integer , nullable=False)
    sharing_type = Column(Integer , nullable=False)
    is_active = Column(Boolean , default=True)
    created_at = Column(DateTime , server_default=func.now())
