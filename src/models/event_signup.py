from extensions import db


class EventSignup(db.Model):
    __tablename__ = 'event_signups'

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def delete_by_event_and_user(cls, event_id, user_id):
        event_signup = cls.query \
            .filter(EventSignup.event_id == event_id) \
            .filter(EventSignup.user_id == user_id).first()
        event_signup.delete()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
