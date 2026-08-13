from sqlalchemy import Column, Integer , ForeignKey , UniqueConstraint
from app.database import Base

class RoomPricing(Base):
    __tablename__ = "room_pricing"
    __table_args__ = (
    UniqueConstraint(
        "owner_id",
        "sharing_type",
        name="uq_owner_sharing_type"
    ),
)

    id = Column(Integer , primary_key=True , index=True)
    owner_id = Column(Integer , ForeignKey("users.id"), nullable=False)
    sharing_type = Column(Integer , nullable=False)
    monthly_rent = Column(Integer , nullable= False)
    deposite = Column(Integer , nullable=False)   