import falcon
import falcon_jsonify
from model import Session, Customer
from hook import validator
from form.customer import CustomerSchema


class CustomerCollectionResource(object):
    """CustomerCollectionResource class handles the endpoints for listing customers"""

    def on_get(self, req, resp):
        dbsession = Session()
        customers = dbsession.query(Customer).all()
        resp.status = falcon.HTTP_200
        customers = [dict(
            id=row.id,
            name=row.name,
            dob=row.dob.strftime('%Y-%m-%d')
        ) for row in customers]
        resp.json = customers
        dbsession.close()

    @falcon.before(validator, CustomerSchema(strict=True))
    def on_post(self, req, resp):
        new_customer = Customer(
            name=req.get_json('name'),
            dob=req.get_json('dob')
        )
        dbsession = Session()
        dbsession.add(new_customer)
        dbsession.commit()
        resp.json = dict(
            id=new_customer.id,
            name=new_customer.name,
            dob=new_customer.dob.strftime('%Y-%d-%m')
        )
        dbsession.close()


class CustomerSingleResource(object):
    """CustomerSingleResource class handles the enpoints for single customers"""

    def on_get(self, req, resp, id):
        dbsession = Session()
        customer = dbsession.query(Customer).filter(Customer.id == id).first()
        if customer is None:
            raise falcon.HTTPNotFound()
        resp.json = dict(
            id=customer.id,
            name=customer.name,
            dob=customer.dob.strftime('%Y-%m-%d')
        )
        dbsession.close()

    @falcon.before(validator, CustomerSchema(strict=True))
    def on_put(self, req, resp, id):
        dbsession = Session()
        customer = dbsession.query(Customer).filter(Customer.id == id).first()
        if customer is None:
            raise falcon.HTTPNotFound()
        customer.name = req.get_json('name')
        customer.dob = req.get_json('dob')
        if len(dbsession.dirty) > 0:
            dbsession.commit()
        resp.json = dict(
            id=customer.id,
            name=customer.name,
            dob=customer.dob.strftime('%Y-%d-%m')
        )


api = application = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True)
])
api.add_route('/customer', CustomerCollectionResource())
api.add_route('/customer/{id:int}', CustomerSingleResource())
