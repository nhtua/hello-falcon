from marshmallow import fields, Schema


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
