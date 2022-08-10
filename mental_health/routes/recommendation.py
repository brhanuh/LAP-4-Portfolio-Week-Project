from cgi import test
import json
from mental_health.models.user import User, Post
from flask import Blueprint, request, render_template, jsonify, session
from ..database.db import db, datetime
# from flask_login import login_user, logout_user, login_required, current_user
from flask_jwt_extended import jwt_required, get_jwt_identity

recom_route = Blueprint("recommendation", __name__)

# show all posts by all users
@recom_route.route("/", methods=["GET"])
@jwt_required()
def all__posts():
    
    posts = Post.query.all()

    get_data = []
    for post in posts:
        get_data.append({
                "posted_user": post.user.username,
                "id": post.id, 
                "type": post.type, 
                "source": post.source, 
                "text":post.text,
                "date_created":post.date_created
                })
    return get_data


#logged in user is able to create a post
@recom_route.route("/post", methods=["POST"])
@jwt_required()
def create_post():
    if request.method == 'POST':
        type = request.json.get('type')
        source = request.json.get('source')
        text = request.json.get('text')

        user = User.query.filter_by(username=get_jwt_identity()).first()
       
        new_post = Post(type=type, source=source, text=text, creator=user.id)
        db.session.add(new_post)
        db.session.commit()
        return 'post created'

                



