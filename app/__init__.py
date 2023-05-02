from imp import init_builtin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.controllers import defaut


def test_connection(self):
    with app.app_context():
        db.app = app
        db.init_app(app)
        db.create_all()
        app.runserver()
        
