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

# to update MAILGUN_API_KEY
vim .env

# start the app
flask run

# to access swagger docs, there are 2 tags: event and event_signup
http://localhost:5000/apidocs/

# import postman collection, there are 2 folders: event and event_signup
eventie.postman_collection.json 
```


### TODO
- Async the mail notification with Celery, need to set up message broker 
- Use uuid for event_id, make it hard to guess the id

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

### update db after model is changed
```angular2html
cd src

FLASK_APP=app.py flask db migrate
flask db upgrade
```



