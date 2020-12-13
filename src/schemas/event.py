from marshmallow import Schema, fields, post_dump, validate, ValidationError, validates_schema


class EventSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=[validate.Length(max=100)])
    location = fields.String(validate=[validate.Length(max=100)])
    description = fields.String(validate=[validate.Length(max=1000)])
    start_time = fields.DateTime(format='%Y-%m-%dT%H:%M:%S')
    end_time = fields.DateTime(format='%Y-%m-%dT%H:%M:%S')
    is_publish = fields.Boolean(dump_only=True)
    is_delete = fields.Boolean(dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    # @post_dump(pass_many=True)
    # def wrap(self, data, many, **kwargs):
    #     if many:
    #         return {'data': data}
    #     return data
