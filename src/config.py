import os
from datetime import datetime


class Config:
    # TODO
    DEBUG = True

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'evite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
