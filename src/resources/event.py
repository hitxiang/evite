from flask import request
from flask_restful import Resource
from http import HTTPStatus
from datetime import datetime

from models.event import Event
from schemas.event import EventSchema

event_schema = EventSchema()
event_list_schema = EventSchema(many=True)

datetime_format = '%Y%m%dT%H%M%S'
class EventListResource(Resource):
    def get(self, datetime_str=None):
        if datetime_str:
            try:
                target_dt = datetime.strptime(datetime_str, datetime_format)
            except ValueError:
                return {'message': 'Wrong input: [%s] for format(%s)' % (datetime_str, datetime_format)},\
                       HTTPStatus.BAD_REQUEST
        else:
            target_dt = datetime.now()

        events = Event.active_list(target_dt)
        return event_list_schema.dump(events), HTTPStatus.OK

    def post(self):
        json_data = request.get_json()
        data, errors = event_schema.load(data=json_data)
        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        event = Event(**data)
        event.save()
        return event_schema.dump(event), HTTPStatus.CREATED


class EventResource(Resource):
    def get(self, event_id):
        event = Event.get_by_id(event_id)
        if event is None:
            return {'message': 'event not found'}, HTTPStatus.NOT_FOUND

        return event_schema.dump(event), HTTPStatus.OK

    def patch(self, event_id):
        json_data = request.get_json()

        data, errors = event_schema.load(data=json_data,
                                         partial=('name','description','start_time','end_time',))

        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        event = Event.get_by_id(event_id)

        if event is None:
            return {'message': 'Event not found'}, HTTPStatus.NOT_FOUND

        event.name = data.get('name') or event.name
        event.description = data.get('description') or event.description
        event.location = data.get('location') or event.location
        event.start_time = data.get('start_time') or event.start_time
        event.end_time = data.get('end_time') or event.end_time

        event.save()

        return event_schema.dump(event), HTTPStatus.OK

    def delete(self, event_id):
        event = Event.get_by_id(event_id)

        if event is None:
            return {'message': 'Event not found'}, HTTPStatus.NOT_FOUND

        event.delete()

        return {}, HTTPStatus.NO_CONTENT
