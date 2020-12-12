### Setup development environment
```
# move to project root
cd evite

virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

### Flask-migration
```angular2html
cd src
flask db init

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
