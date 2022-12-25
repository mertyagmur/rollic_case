from flask import abort, make_response, jsonify
from app import db
from .models import *

def get_all():
    users = User.query.all()
    return users_schema.dump(users), 200
    

def create(user):
    email = user.get("email")
    existing_user = User.query.filter(User.email == email).one_or_none()
    errors = user_schema.validate(user)

    if errors:
        return jsonify({"error": "Bad request"}), 400
    elif existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"id": new_user.id, "name": new_user.name, "email": new_user.email}), 200
    elif existing_user is not None:
        return jsonify({"error": "User with that email already exists"}), 403
    else:
        return jsonify({"error": "server error"}), 500
    
def get_one(id):
    user = User.query.filter(User.id == id).one_or_none()

    if user is not None:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    elif user is None:
        return jsonify({"error": "User with that id does not exist"}), 404
    else:
        return jsonify({"error": "server error"}), 500

def update(id, user):
    existing_user = User.query.filter(User.id == id).one_or_none()
    errors = user_schema.validate(user)

    if errors:
        return jsonify({"error": "Bad request"}), 400
    elif existing_user is not None:
        update_user = user_schema.load(user, session=db.session)
        existing_user.name = update_user.name
        existing_user.email = update_user.email
        existing_user.password = update_user.password
        db.session.merge(existing_user)
        db.session.commit()
        return jsonify({"id": existing_user.id, "name": existing_user.name, "email": existing_user.email}), 200
    elif existing_user is None:
        return jsonify({"error": "User with that it does not exist"}), 404
    else:
        return jsonify({"error": "server error"}), 500

def delete(id):
    existing_user = User.query.filter(User.id == id).one_or_none()
    
    if existing_user is not None:
        db.session.delete(existing_user)
        db.session.commit()
        return jsonify({"message": "User deletion is successful"}), 200
    elif existing_user is None:
        return jsonify({"error": "User with that it does not exist"}), 404
    else:
        return jsonify({"error": "server error"}), 500