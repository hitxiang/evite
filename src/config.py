import os
import logging

logging.basicConfig()
# TODO should dynamically based on environment
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


class Config:
    # TODO
    DEBUG = True

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'evite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # TODO move to config files
    MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')
    MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
    PREDEFINED_MAIL = os.getenv('PREDEFINED_MAIL')