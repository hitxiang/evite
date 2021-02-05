from flask import request, current_app
from flask_restful import Resource
from http import HTTPStatus

from models.event import Event
from models.event_signup import EventSignup
from models.user import User

from utils.mailgun import MailgunApi
import logging

_logger = logging.getLogger(__name__)


# TODO send mail asynchronously
def send_mail_notification(email, event_id, event_name):
    mailgun = MailgunApi(domain=current_app.config['MAILGUN_DOMAIN'],
                         api_key=current_app.config['MAILGUN_API_KEY'])

    receipt = current_app.config['PREDEFINED_MAIL']
    mail_text = '[%s] sign up event[%d: %s]' % (email, event_id, event_name)
    _logger.info("mail [%s] to %s", mail_text, receipt)
    response = mailgun.send_email(to=receipt,
                       subject='New SignUp',
                       text=mail_text)

    return response.status_code == 200


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

        email = json_data['email']
        user = _get_or_create_user(email)
        es = EventSignup.find_by_event_and_user(event_id, user.id)
        if es is not None:
            return {'message': 'Already signed up'}, HTTPStatus.BAD_REQUEST

        event.users.append(user)
        event.save()
        ok = send_mail_notification(email, event_id, event.name)
        if not ok:
            _logger.warning("mail to %s is failed for %d", email, event_id)
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

        es = EventSignup.find_by_event_and_user(event_id, user.id)
        if es is None:
            return {'message': 'No signup yet'}, HTTPStatus.BAD_REQUEST
        es.delete()
        return {}, HTTPStatus.NO_CONTENT
