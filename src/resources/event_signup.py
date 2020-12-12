from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.event import Event
from models.event_signup import EventSignup
from models.user import User


class EventSignupResource(Resource):

    def put(self, event_id):
        event = Event.get_by_id(event_id)

        if event is None:
            return {'message': 'event not found'}, HTTPStatus.NOT_FOUND

        json_data = request.get_json()
        if not json_data or not json_data['email']:
            # TODO validate the email address
            return {'message': 'email is required'}, HTTPStatus.BAD_REQUEST

        user = self._get_or_create_user(json_data['email'])

        event.users.append(user)
        event.save()
        return {}, HTTPStatus.NO_CONTENT

    def delete(self, event_id):
        event = Event.get_by_id(event_id)

        if event is None:
            return {'message': 'event not found'}, HTTPStatus.NOT_FOUND

        json_data = request.get_json()
        if not json_data or not json_data['email']:
            # TODO validate the email address
            return {'message': 'email is required'}, HTTPStatus.BAD_REQUEST

        user = User.get_by_email(json_data['email'])
        if user is None:
            return {'message': 'No signup for the event'}, HTTPStatus.NOT_FOUND

        EventSignup.delete_by_event_and_user(event_id, user.id)
        return {}, HTTPStatus.NO_CONTENT

    def _get_or_create_user(self, email):
        user = User.get_by_email(email)
        if user is None:
            user = User(email=email)
            user.save()
        return user
