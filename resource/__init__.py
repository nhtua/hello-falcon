from model.database import DBManager


class BaseResource(object):
    def __init__(self, db_manager: DBManager):
        self.db = db_manager
