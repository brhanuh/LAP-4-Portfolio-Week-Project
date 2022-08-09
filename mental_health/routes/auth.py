import json
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta, timezone

from sqlalchemy.exc import IntegrityError
from ..models.user import User
from ..database.db import db
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask_jwt_extended import jwt_required
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == 'POST':
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

        hashed_pass = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, hash_password=hashed_pass)
        db.session.add(new_user)
        db.session.commit()
        return 'User Created'
    
    if request.method == 'GET':
        users = User.query.all()

        all_data =[]
        for user in users:
            all_data.append({
                "id": user.id, 
                "username": user.username, 
                "email": user.email, 
                "password":user.hash_password})
        return all_data


@auth_routes.route("/login", methods=["POST"])
def login():
    if request.method == 'POST':
        username = request.json.get("username")
        password = request.json.get("password")

        user = User.query.filter_by(username=username).first()

        #hash password first and then the userinput password
        if user:
            if not check_password_hash(user.hash_password, password):
                return 'incorrect password'
            # login_user(user, remember=True)
            # return 'user logged in' 
            access_token = create_access_token(identity=username)
            response = {"access_token":access_token, "user_id": user.id, "username": user.username}
            return response 
        return 'no such user'
        
    
# @auth_routes.route("/logout", methods=["POST"])
# def logout():
#     response = jsonify({"msg": "logout successful"})
#     unset_jwt_cookies(response)
#     return response

# @auth_routes.route("/logout", methods = ["POST"])
# @logout_user
# def logout():
#     logout_user()
#     return 'user logged out'
# #     #redirect(url_for(""))
    

   

##### experimenting with a protected endpoint #####             

@auth_routes.route('/profile')
@jwt_required()
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body 


