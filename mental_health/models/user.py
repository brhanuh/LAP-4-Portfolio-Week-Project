from ..database.db import db
from time import timezone
from sqlalchemy.sql import func



class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    hash_password = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='user')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    type = db.Column(db.String(100), default="")
    source = db.Column(db.String(100), default="")
    text = db.Column(db.Text(), default="")
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    creator = db.Column(db.String(50), db.ForeignKey('user.username'), nullable=False)
