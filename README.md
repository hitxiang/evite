### Setup development environment
```
# move to project root
cd evite

virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

### DB migration and populate data seeds
```angular2html
cd src

# create db schema
flask db upgrade

# populate event list, code is in src/scripts/manager.py#db_seed
# please update src/scripts/manager.py#db_seed to change event list
FLASK_APP=scripts/manager.py flask db_seed
```

### Run and test api
Since we are using sandbox for testing, the Recipients should be authorized first 
in order to receive mails.
now, the only authorized receipt is hitxiang@gmail.com
please update .env to update the predefined mail address
```angular2html
cd src

# start the app
flask run

# to access swagger docs
http://localhost:5000/apidocs/
```

### Rest api docs
```angular2html
http://127.0.0.1:5000/events/20210102T123000
```

### TODO
- Async the mail notification with Celery, need to set up message broker 

## Others
### SQLAlchemy python console
```
from app import create_app
app = create_app()
app.app_context().push()

from models.event import Event
event = Event(name='test01')
event.save()
```



