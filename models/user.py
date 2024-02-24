from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date,default=datetime.utcnow)


    def __refr__(self):
        return f"<User:{self.name}>"
    
    def to_dict(self):
        data = dict(self.__dict__)
        del data['_sa_instance_state']
        return data
    