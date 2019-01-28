import falcon
import json
from model import Session, Customer

class CustomerCollectionResource(object):
    """CustomerCollectionResource class handles the endpoints for listing customers"""

    def on_get(self, req, resp):
        dbsession = Session()
        customers = dbsession.query(Customer).all()
        resp.status = falcon.HTTP_200
        customers = [dict(
            id  =row.id,
            name=row.name,
            dob =row.dob.strftime('%Y-%m-%d')
        ) for row in customers]
        resp.content_type = falcon.MEDIA_JSON
        resp.body = json.dumps(customers)
        dbsession.close()


class CustomerSingleResource(object):
    """CustomerSingleResource class handles the enpoints for single customers"""
    def on_get(self, req, resp, id):
        dbsession = Session()
        customer = dbsession.query(Customer).filter(Customer.id == id).first()
        if customer is None:
            raise falcon.HTTPNotFound()
        resp.content_type = falcon.MEDIA_JSON
        resp.body = json.dumps(dict(
            id  = customer.id,
            name= customer.name,
            dob = customer.dob.strftime('%Y-%m-%d')
        ))
        dbsession.close()


api = application = falcon.API()
api.add_route('/customer', CustomerCollectionResource())
api.add_route('/customer/{id:int}', CustomerSingleResource())
