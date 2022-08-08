import json
from flask import Blueprint, jsonify, request, abort, render_template
import bcrypt
from sqlalchemy.exc import IntegrityError
from ..models.user import User
from ..database.db import db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

auth_routes = Blueprint("auth", __name__)
token_route = Blueprint("token", __name__)
login_route = Blueprint("login", __name__)

# Creating a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@token_route.route("/login", methods=["POST"])
def token():
    if request.method == "POST":
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        if username != "test" or password != "test":
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=username)

        return jsonify(access_token=access_token)



@auth_routes.route("/register", methods = ["POST", "GET"])
def register():
    try:
        if request.method == "POST":
            username = request.json.get('username',None)
            email = request.json.get('email',None)
            password = request.json.get('password',None)

            if not username:
                return 'Missing username', 400
            if not email:
                    return 'Missing email', 400
            if not password:
                return 'Missing password', 400

            # user_exists = User.query.filter_by(email=email).first() is not None

            # if user_exists:
            #     abort(409)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            new_user = User(username=username, email=email, hash_password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            return "user created"
        
    except AttributeError:
        return "Please provide email and pass as JSON", 400
    except IntegrityError:
        return "The User is already registered", 400
        
   
    if request.method == "GET":
        users = User.query.all()

        all_data =[]
        for user in users:
            all_data.append({
                "id": user.id, 
                "username": user.username, 
                "email": user.email, 
                "password":user.hash_password})
        return all_data
                   
               
            


# @login_route.route("/login", methods=['POST'])
# def login():
#     email = request.json.get('email', None)
#     password = request.json.get('password', None)

#     if not email:
#         return 'Missing email', 400
#     if not password:
#         return 'Missing password', 400
    
#     #query the database
#     user = User.query.filter_by(email=email).first()
#     #if the user does not exist 
#     if not user:
#         return f'User Not Found', 404
    
#     #if the user exists, check if passwords match
#     if bcrypt.checkpw(password.encode('utf-8'), user.hash_password):
#         return f'Welcome back'
#     else:
#         return "Wrong password!"
    
            