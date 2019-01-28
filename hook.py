from marshmallow import Schema, ValidationError
import falcon


def validator(req, resp, resource, params, schema: Schema):
    data = req.json
    try:
        schema.load(data)
    except ValidationError as err:
        print(err.messages)
        raise falcon.HTTPBadRequest(title="Validator Error", description=err.messages)
