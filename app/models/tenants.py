from app.database import Base
from sqlalchemy import Column , String , Integer , DateTime,ForeignKey , Boolean , Date
from sqlalchemy.sql import func

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer , primary_key= True , index=True)
    bed_id = Column(Integer , ForeignKey("beds.id"), nullable=False)
    full_name = Column(String(20) , nullable=False)
    phone_number = Column(String(15), unique=True , nullable=False)
    aadhar_number= Column(String(20),unique=True, nullable=False)
    join_date = Column(Date , nullable=False)
    leave_date = Column(Date , nullable=True)
    deposit_paid = Column(Integer , nullable=False)
    is_active = Column(Boolean , default=True)
    created_at = Column(DateTime , server_default=func.now())
