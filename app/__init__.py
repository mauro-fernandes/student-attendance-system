from imp import init_builtin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine


app = Flask(__name__)

app.config.from_object('config')

## sqlite://<nohostname>/<path>
## where <path> is relative:
engine = create_engine("sqlite:///storage.sqlite3")

db = SQLAlchemy(app)

#db.app = app
#db.init_app(app)
#db.create_all()
#


'''def setup_db(app, database_path='sqlite:///DB.sqlite3'):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.app = app
    db.init_app(app)
    db.create_all()'''


migrate = Migrate(app, db)

#app.add_command('db',  )



from app.controllers import defaut




def test_connection(self):
    with app.app_context():
        db.create_all()
        app.runserver()
        #test code
        


if __name__ == "__main__":
    db.create_all()
    app.runserver()