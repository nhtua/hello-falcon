from sqlalchemy import Column, Integer, TIMESTAMP, String, Date
from model.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'user'
    id         = Column(Integer, primary_key=True, autoincrement=True)
    username   = Column(String(64))
    password   = Column(String(64))
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    updated_at = Column(TIMESTAMP)
