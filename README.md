### Setup development environment
```
# move to project root
cd evite

virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

### Run the command
```angular2html
cd src

# create db schema
flask db upgrade

# populate event list, code is in src/scripts/manager.py#db_seed
FLASK_APP=scripts/manager.py flask db_seed
```

### Flask-migration
```angular2html
cd src

# no need to execute
flask db init

flask db migrate
flask db upgrade


```

### SQLAlchemy python console
```
from app import create_app
app = create_app()
app.app_context().push()

from models.event import Event
event = Event(name='test01')
event.save()
```
