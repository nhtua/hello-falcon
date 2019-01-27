import falcon


class CustomerResource(object):
    """CustomerResource class handles the CRUD endpoints for managing customer's information"""

    def on_get(self, req, resp):
        resp.status = "200 OK"
        resp.body = "hello world"


api = application = falcon.API()
customers_resource = CustomerResource()
api.add_route('/customer', customers_resource)