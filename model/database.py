from config import cfg
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(cfg('database', 'connection_string'),
                       pool_recycle=3600,
                       echo=True,
                       pool_size=10,
                       max_overflow=20,
                       pool_timeout=30)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d
