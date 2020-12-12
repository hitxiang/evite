from marshmallow import Schema, fields


class UserSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)