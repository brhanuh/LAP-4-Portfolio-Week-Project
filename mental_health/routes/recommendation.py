import json
from mental_health.models.user import User, Post
from xml.dom import NotFoundErr
from flask import Blueprint, request
from ..database.db import db
from werkzeug import exceptions
from flask_jwt_extended import jwt_required, get_jwt_identity

recom_route = Blueprint("recommendation", __name__)

# show all posts by all users (must be logged in)
@recom_route.route("/", methods=["GET"])
@jwt_required()
def all__posts():
    try:
        posts = Post.query.order_by(Post.id.desc()).all()

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
    
    except NotFoundErr as err:
        raise exceptions.NotFound

#view all posts by username, must be logged in
@recom_route.route("/post/<string:username>", methods=['GET'])
@jwt_required()
def post_byid(username):
    try:
        user = User.query.filter_by(username=username).first()

        if user.username == get_jwt_identity():
            posts = Post.query.order_by(Post.date_created.desc()).all()

            user_posts = []
            for post in posts:
                if post.user.username == get_jwt_identity():
                    user_posts.append({
                        "posted_user_POST": post.user.username,
                        "id": post.id, 
                        "type": post.type, 
                        "source": post.source, 
                        "text":post.text,
                        "date_created":post.date_created,
                    })
            return user_posts
    
    except NotFoundErr as err:
        raise exceptions.NotFound


#logged in user is able to create a post
@recom_route.route("/post", methods=["POST"])
@jwt_required()
def create_post():
    try:
        type = request.json.get('type')
        source = request.json.get('source')
        text = request.json.get('text')

        user = User.query.filter_by(username=get_jwt_identity()).first()
       
        new_post = Post(type=type, source=source, text=text, creator=user.username)
        db.session.add(new_post)
        db.session.commit()
        return 'post created'

    except Exception as err:
        print(err)

                
@recom_route.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400


@recom_route.errorhandler(exceptions.Unauthorized)
def handle_401(err):
    return {'message': f'Not authorized! {err}'}, 401


@recom_route.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


@recom_route.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us {err}"}, 500


