from flask import Flask, init_db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)

def create_app():
    with app.app_context():
        init_db()

    return app




app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date,default=datetime.utcnow)


def __refr__(self):
    return f"<User:{self.name}>"