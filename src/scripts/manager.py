from datetime import datetime, timedelta
from app import create_app
from extensions import db
from models.event import Event


app = create_app()


@app.cli.command('db_seed')
def db_seed():
    now = datetime.strptime('2021-01-01', '%Y-%m-%d')
    event1 = Event(name='event 1',
                   location='Location 1',
                   is_publish=True,
                   description='For python event 01',
                   start_time=datetime.now() - timedelta(days=1, hours=12),
                   end_time=datetime.now() + timedelta(days=1, hours=13),
                   )

    event2 = Event(name='event 2',
                   location='Location 2',
                   description='For python event 02',
                   is_publish=False,
                   start_time=datetime.now() - timedelta(days=1, hours=12),
                   end_time=datetime.now() + timedelta(days=1, hours=13),
                   )

    event3 = Event(name='event 3',
                   location='Location 3',
                   description='For python event 03',
                   is_publish=True,
                   start_time=datetime.now() - timedelta(days=2, hours=12),
                   end_time=datetime.now() + timedelta(days=4, hours=13),
                   )

    event4 = Event(name='event 4',
                   location='Location 4',
                   description='For python event 04',
                   is_publish=True,
                   start_time=now + timedelta(days=3, hours=12),
                   end_time=now + timedelta(days=3, hours=13),
                   )

    event5 = Event(name='event 5',
                   location='Location 5',
                   description='For python event 05',
                   is_publish=True,
                   start_time=now + timedelta(days=1, hours=12),
                   end_time=now + timedelta(days=1, hours=13),
                   )

    event6 = Event(name='event 6',
                   location='Location 6',
                   description='For python event 06',
                   is_publish=True,
                   start_time=now + timedelta(days=1, hours=12),
                   end_time=now + timedelta(days=1, hours=13),
                   )

    event7 = Event(name='event 7',
                   location='Location 7',
                   description='For python event 07',
                   is_publish=True,
                   start_time=now + timedelta(days=1, hours=12),
                   end_time=now + timedelta(days=1, hours=13),
                   )

    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)
    db.session.add(event4)
    db.session.add(event5)
    db.session.add(event6)
    db.session.add(event7)
    db.session.commit()
    print('Database seeded!')
