from app.database import Base
from sqlalchemy import Column , String , Integer , DateTime,ForeignKey , Boolean
from sqlalchemy.sql import func

class Bed(Base):
    __tablename__ = "beds"

    id = Column(Integer , primary_key= True , index=True)
    room_id = Column(Integer , ForeignKey("rooms.id"), nullable=False)
    bed_no = Column(String(10) , nullable=False)
    monthly_rent = Column(Integer , nullable=False)
    deposite = Column(Integer , nullable=False)
    status = Column(Integer , nullable=False)
    is_active = Column(Boolean , default=True)
    created_at = Column(DateTime , server_default=func.now())
