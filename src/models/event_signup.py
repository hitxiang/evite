from extensions import db


class EventSignup(db.Model):
    __tablename__ = 'event_signups'

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
