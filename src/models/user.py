from extensions import db
from models.event_signup import EventSignup


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    events = db.relationship(
        'Event',
        secondary=EventSignup.__tablename__,
        back_populates='users',
    )


