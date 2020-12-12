from extensions import db
from models.event_signup import EventSignup


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime())
    end_time = db.Column(db.DateTime())
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    users = db.relationship(
        'User',
        secondary=EventSignup.__tablename__,
        back_populates='events',
    )
