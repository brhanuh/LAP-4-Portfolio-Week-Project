import json
from flask import Blueprint, request, jsonify
from ..models.user import User
from ..database.db import db
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from werkzeug import exceptions
from werkzeug.security import generate_password_hash, check_password_hash

auth_routes = Blueprint("auth", __name__)

#Register a user
@auth_routes.route("/register", methods = ["POST"])
def register():
    try:
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")

        #checking if a user exists
        user_email = User.query.filter_by(email=email).first()
        user = User.query.filter_by(email=email).first()

        if user_email:
            return 'email already exists'
        elif user:
            return 'username already exists'

        #Hashing the password and storing the user in the database
        hashed_pass = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, hash_password=hashed_pass)
        db.session.add(new_user)
        db.session.commit()
        return 'User Created', 201
    
    except:
        raise exceptions.InternalServerError()
    

#Login route
@auth_routes.route("/login", methods=["POST"])
def login():
    try:
        username = request.json.get("username")
        password = request.json.get("password")

        if not username:
            raise exceptions.BadRequest('No username provided')
        if not password:
            raise exceptions.BadRequest('No password provided')

        user = User.query.filter_by(username=username).first()

        #hash password first and then the userinput password for check_password_hash
        if user:
            if not check_password_hash(user.hash_password, password):
                raise exceptions.Unauthorized('Incorrect password.')
            
        #Create access token if the user input password and database password(hashed) are correct
            access_token = create_access_token(identity=username)
            response = {"access_token":access_token, "user_id": user.id, "username": user.username}
            return response 
        raise exceptions.BadRequest()
    
    except exceptions.BadRequest:
        raise exceptions.BadRequest()
    except exceptions.Unauthorized:
        raise exceptions.Unauthorized('Incorrect password.')
    except:
        raise exceptions.InternalServerError()

@auth_routes.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400


@auth_routes.errorhandler(exceptions.Unauthorized)
def handle_401(err):
    return {'message': f'Not authorized! {err}'}, 401


@auth_routes.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


@auth_routes.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500
