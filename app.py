import falcon
import falcon_jsonify

from model.database import DBManager
from resource.customer import *

dbm = DBManager()
dbm.setup()

api = application = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True)
])
api.add_route('/customer', CustomerCollectionResource(dbm))
api.add_route('/customer/{id:int}', CustomerSingleResource(dbm))
