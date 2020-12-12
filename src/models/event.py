from extensions import db
from models.event_signup import EventSignup


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000), nullable=False)
    start_time = db.Column(db.DateTime(), nullable=False)
    end_time = db.Column(db.DateTime(), nullable=False)
    is_publish = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    users = db.relationship(
        'User',
        secondary=EventSignup.__tablename__,
        back_populates='events',
    )

    @classmethod
    def active_list(cls, target_dt):
        # TODO stop signup x minutes ahead of end_time
        return cls.query\
            .filter(Event.start_time < target_dt)\
            .filter(Event.end_time > target_dt)\
            .all()

    @classmethod
    def get(cls, event_id):
        return cls.query.get(event_id)


    def save(self):
        db.session.add(self)
        db.session.commit()
