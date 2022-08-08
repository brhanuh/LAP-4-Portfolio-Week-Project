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
from werkzeug.security import generate_password_hash, check_password_hash

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        #checking if a user exists
        user_email = User.query.filter_by(email=email).first()
        user = User.query.filter_by(email=email).first()

        if user_email:
            return 'email already exists'
        elif user:
            return 'username already exists'
        else:
            new_user = User(username=username, email=email, hash_password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'User Created'
    
    if request.method == 'GET':
        user = User.query.all()

        all_users = []
        return (
            all_users.append({
                "username": user.username,
                "email": user.email,
                "password": user.hash_password,
            })
        )




@auth_routes.route("/login", methods=["POST"])
def login():
    return "Hello login"
        



@auth_routes.route("/logout", methods = ["POST"])
def logout():
    return "Hello logout"
    

   

##### experimenting with a protected endpoint #####             

# @auth_routes.route('/profile')
# @jwt_required()
# def my_profile():
#     response_body = {
#         "name": "Nagato",
#         "about" :"Hello! I'm a full stack developer that loves python and javascript"
#     }

#     return response_body 


