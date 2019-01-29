import falcon
import falcon_jsonify

from middleware.AuthMiddleware import AuthMiddleware
from model.database import DBManager
from resource.auth import Auth
from resource.customer import *

dbm = DBManager()
dbm.setup()

api = application = falcon.API(middleware=[
    AuthMiddleware(exclude_routes=['/auth']),
    falcon_jsonify.Middleware(help_messages=True),
])

api.add_route('/auth', Auth(dbm))
api.add_route('/customer', CustomerCollectionResource(dbm))
api.add_route('/customer/{id:int}', CustomerSingleResource(dbm))
