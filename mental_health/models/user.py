from ..database.db import db
from uuid import uuid4


# def get_uuid():
#     return uuid4().hex

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    hash_password = db.Column(db.String(128), nullable=False)


