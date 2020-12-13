from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.event import Event
from models.event_signup import EventSignup
from models.user import User


def _get_or_create_user(email):
    user = User.get_by_email(email)
    if user is None:
        user = User(email=email)
        user.save()
    return user


class EventSignupResource(Resource):

    def put(self, event_id):
        """
        To signup event by id
        ---
        tags:
          - event_signup
        parameters:
          - in: path
            name: event_id
            required: true
            description: The ID of the event, try 1!
            type: integer
          - in: body
            name: body
            schema:
              properties:
                email:
                  type: string
                  required: true
                  description: the email to cancel from event
        responses:
          204:
            description: Event signed up
        """
        event = Event.get_by_id(event_id)

        if event is None:
            return {'message': 'event not found'}, HTTPStatus.NOT_FOUND

        json_data = request.get_json()
        if not json_data or not json_data['email']:
            # TODO validate the email address
            return {'message': 'email is required'}, HTTPStatus.BAD_REQUEST

        user = _get_or_create_user(json_data['email'])
        es = EventSignup.find_by_event_and_user(event_id, user.id)
        if es is not None:
            return {'message': 'Already signed up'}, HTTPStatus.NO_CONTENT

        event.users.append(user)
        event.save()
        return {}, HTTPStatus.NO_CONTENT

    def delete(self, event_id):
        """
        To cancel event by id
        ---
        tags:
          - event_signup
        parameters:
          - in: path
            name: event_id
            required: true
            description: The ID of the event, try 1!
            type: integer
          - in: body
            name: body
            schema:
              properties:
                email:
                  type: string
                  required: true
                  description: the email to cancel from event
        responses:
          204:
            description: Event canceled
        """
        event = Event.get_by_id(event_id)

        if event is None:
            return {'message': 'event not found'}, HTTPStatus.NOT_FOUND

        json_data = request.get_json()
        if not json_data or not json_data['email']:
            # TODO validate the email address
            return {'message': 'email is required'}, HTTPStatus.BAD_REQUEST

        user = User.get_by_email(json_data['email'])
        if user is None:
            return {'message': 'No signup exists for the event'}, HTTPStatus.NOT_FOUND

        EventSignup.delete_by_event_and_user(event_id, user.id)
        return {}, HTTPStatus.NO_CONTENT
