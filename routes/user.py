from app import app, db
from flask import render_template, request
from models.user import User
'''
USER RECORD GET ALL
USER RECORD GET - ONE
USER RECORD INSERT
USER RECORD UPDATE
USER RECORD DELETE
'''
@app.route("/user", methods=['GET', 'POST'])
def user():
    if request.method=='GET':
        # all records
        users = User.query.all() # array of records
        return {"data": [u.to_dict() for u in users]}
    elif request.method=='POST':
        '''
        Create record in table
        '''
        data = request.get_json()
        name = data["name"]
        email = data["email"]
        user = User(
            name=name,
            email=email
        )
        db.session.add(user)
        db.session.commit()
        return {"status":"Record is created."}

@app.route("/user/<id>", methods=['PUT', 'DELETE'])
def userUpdate(id):
    if request.method=='PUT':
        user = User.query.filter_by(id=id).first() # array of records
        json = request.get_json()
        user.name = json["name"]
        db.session.commit()
        return {"status":"Record is update."}
    elif request.method=='DELETE':
        user = User.query.filter_by(id=id).first() # array of records
        db.session.delete(user)
        db.session.commit()
        return {"status":"Record is deleted."}

