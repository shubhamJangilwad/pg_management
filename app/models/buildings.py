from app.database import Base
from sqlalchemy import Column, Integer , String , DateTime , ForeignKey
from sqlalchemy.sql import func

class Building(Base):
    __tablename__ = "pg_building"

    id = Column(Integer , primary_key=True, index=True)
    owner_id = Column(Integer ,ForeignKey("users.id"),nullable=False)
    building_name = Column(String(100) , nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    total_floors = Column(Integer , nullable=False)
    created_at = Column(DateTime , server_default=func.now())



