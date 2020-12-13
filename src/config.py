import logging
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


logging.basicConfig()
# TODO should dynamically based on environment
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


class Config:
    DEBUG = environ.get('DEBUG').lower() == 'true'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'evite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAILGUN_DOMAIN = environ.get('MAILGUN_DOMAIN')
    MAILGUN_API_KEY = environ.get('MAILGUN_API_KEY')
    PREDEFINED_MAIL = environ.get('PREDEFINED_MAIL')