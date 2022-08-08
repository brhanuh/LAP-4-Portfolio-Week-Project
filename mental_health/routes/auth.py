import json
from flask import Blueprint, jsonify, request, abort, render_template
import bcrypt
from datetime import datetime, timedelta, timezone

from sqlalchemy.exc import IntegrityError
from ..models.user import User
from ..database.db import db
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask_jwt_extended import jwt_required

auth_routes = Blueprint("auth", __name__)

@auth_routes.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

# Creating a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@auth_routes.route("/login", methods=["POST", "GET"])
def token():
    if request.method == "POST":
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        
        user = User.query.filter_by(username=username).first()

        # return jsonify ({
        #     "username": user.username,
        #     "password": user.hash_password
        # })

        # if not bcrypt.checkpw(password.encode('utf-8'), user.hash_password):
        #   return f'Welcome back {username}'
        # else:
        #   return "Wrong password!"

        if username != user.username:
            return ({"msg": "Wrong email or password"}), 401

        access_token = create_access_token(identity=username)

        return jsonify(access_token=access_token)
    
    # if request.method == "GET":
    #     username = "test"
    #     user = User.query.filter_by(username=username).first()
    #     print(user)


@auth_routes.route("/logout", methods = ["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

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

##### experimenting with a protected endpoint #####             

# @auth_routes.route('/profile')
# @jwt_required()
# def my_profile():
#     response_body = {
#         "name": "Nagato",
#         "about" :"Hello! I'm a full stack developer that loves python and javascript"
#     }

#     return response_body 


