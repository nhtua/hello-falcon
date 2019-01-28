import falcon
import falcon_jsonify
from resource.customer import *


api = application = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True)
])
api.add_route('/customer', CustomerCollectionResource())
api.add_route('/customer/{id:int}', CustomerSingleResource())
