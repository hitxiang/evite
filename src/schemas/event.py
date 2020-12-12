from marshmallow import Schema, fields, post_dump, validate, ValidationError, validates_schema


class EventSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=[validate.Length(max=100)])
    location = fields.String(validate=[validate.Length(max=100)])
    description = fields.String(validate=[validate.Length(max=1000)])
    start_time = fields.DateTime()
    end_time = fields.DateTime()
    is_publish = fields.Boolean(dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    # @post_dump(pass_many=True)
    # def wrap(self, data, many, **kwargs):
    #     if many:
    #         return {'data': data}
    #     return data

    @validates_schema
    def validate_times(self, data, **kwargs):
        if data["start_time"] >= data["end_time"]:
            raise ValidationError("end_time must be greater than start_time")