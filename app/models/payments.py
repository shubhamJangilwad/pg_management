from app.database import Base
from sqlalchemy import Column , String , Integer , DateTime,ForeignKey , Boolean , Date
from sqlalchemy.sql import func

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer , primary_key= True , index=True)
    tenant_id = Column(Integer , ForeignKey("tenants.id"), nullable=False)
    payment_month = Column(String(10) , nullable=False)
    amount = Column(Integer , nullable=False)
    payment_date = Column(Date , nullable=False)
    payment_status = Column(String(20) , nullable=False)
    refund_amount = Column(Integer , nullable=True)
    maintenance_charge = Column(Integer, nullable=True)
    is_active = Column(Boolean , default=True)
    created_at = Column(DateTime , server_default=func.now())
