from sqlalchemy import Column, Integer, TIMESTAMP, String, Date, JSON
from model.database import Base


class Customer(Base):
    __tablename__ = 'customer'
    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String(64))
    dob        = Column(Date)
    meta       = Column(JSON)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
