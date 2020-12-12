from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)


if __name__ == '__main__':
    app = create_app()
    app.run()