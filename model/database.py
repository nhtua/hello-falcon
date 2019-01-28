from config import cfg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoping
import model


class DBManager(object):
    def __init__(self):
        self.engine = create_engine(cfg('database', 'connection_string'),
                                    pool_recycle=3600,
                                    echo=True,
                                    pool_size=10,
                                    max_overflow=20,
                                    pool_timeout=30)
        self.DBSession = scoping.scoped_session(
            sessionmaker(
                bind=self.engine,
                autocommit=False
            )
        )

    @property
    def session(self):
        """See this doc"""
        """https://docs.sqlalchemy.org/en/rel_1_2/orm/contextual.html#sqlalchemy.orm.scoping.scoped_session"""
        return self.DBSession()

    def setup(self):
        """Run this funciton to generate database"""
        try:
            model.BaseModel.metadata.create_all(self.engine)
        except Exception as e:
            print('Could not initialize DB: {}'.format(e))
