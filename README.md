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
FLASK_APP=scripts/manager.py flask db_seed
```

### Run and test api
Since we are using sandbox for testing, the Recipients should be authorized first 
in order to receive mails.
now, the only authorized receipt is hitxiang@gmail.com
```angular2html
cd src

export MAILGUN_DOMAIN=sandbox7a50d70271ad4a2f8409d6d0297a833c.mailgun.org
export MAILGUN_API_KEY=5b8bd6b9cc9241a0ec54f651de502a56-4879ff27-e4cb66df
export PREDEFINED_MAIL=hitxiang@gmail.com

# start the app
flask run

# to access swagger docs
http://localhost:5000/apidocs/
```

### Rest api docs
```angular2html
http://127.0.0.1:5000/events/20210102T123000
```

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



