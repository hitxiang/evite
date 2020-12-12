from flask import request
from flask_restful import Resource
from http import HTTPStatus
from datetime import datetime

from models.event import Event


class EventListResource(Resource):
    def get(self):
        # TODO
        data = Event.active_list(datetime.now())

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        recipe = Event(name=data['name'],
                       location=data['location'],
                       description=data['description'],
                       start_time=data['start_time'],
                       end_time=data['end_time'])

        return recipe.data, HTTPStatus.CREATED


class EventResource(Resource):

    def get(self, event_id):
        event = None
        if event is None:
            return {'message': 'event not found'}, HTTPStatus.NOT_FOUND

        return {}, HTTPStatus.OK

    def put(self, event_id):
        return {}, HTTPStatus.OK

    def delete(self, event_id):
        return {}, HTTPStatus.NO_CONTENT
