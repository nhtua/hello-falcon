import falcon
import json
from model import Session, Customer, row2dict


class CustomerResource(object):
    """CustomerResource class handles the CRUD endpoints for managing customer's information"""

    def on_get(self, req, resp):
        dbsession = Session()
        customers = dbsession.query(Customer).all()
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.body = json.dumps([row2dict(row) for row in customers])
        dbsession.close()


api = application = falcon.API()
customers_resource = CustomerResource()
api.add_route('/customer', customers_resource)