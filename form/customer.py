from marshmallow import fields, Schema


class CustomerSchema(Schema):
    name    = fields.Str(required=True)
    dob     = fields.Date(required=True)
