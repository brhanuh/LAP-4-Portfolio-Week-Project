from cgi import test
import json
from mental_health.models.user import User, Post
from flask import Blueprint, request, render_template, jsonify, session
from ..database.db import db, datetime
# from flask_login import login_user, logout_user, login_required, current_user
from flask_jwt_extended import jwt_required, get_jwt_identity

recom_route = Blueprint("recommendation", __name__)


@recom_route.route("/posts", methods=["POST","GET"])
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

    if request.method == 'GET':
        return 'should redirect to the all posts page'
                



