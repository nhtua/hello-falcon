from sqlalchemy import Column, Integer, TIMESTAMP, String, Date, JSON
from model.BaseModel import BaseModel
from datetime import datetime


class Customer(BaseModel):
    __tablename__ = 'customer'
    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String(64))
    dob        = Column(Date)
    meta       = Column(JSON)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    updated_at = Column(TIMESTAMP)
