from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, request
from flask_jwt_extended import JWTManager

from flask_cors import CORS

from .database.db import db
from .routes.main import main_routes
from .routes.auth import auth_routes
# from .routes.auth import token_route
from .routes.auth import login_route

# load environment
load_dotenv()

database_uri = environ.get('DATABASE_URL')

if 'postgres:' in database_uri:
    database_uri = database_uri.replace("postgres:", "postgresql:")

# Set up the app

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "dakzbakz12345tok"  # Change this!
jwt = JWTManager(app)

app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'),
    SECRET_KEY="87sdf9oasdfhy90p@fd9" #a random key I entered
)


CORS(app)
db.app = app
db.init_app(app)

app.register_blueprint(main_routes)
app.register_blueprint(auth_routes)
# app.register_blueprint(token_route)
app.register_blueprint(login_route)

## Main

if __name__ == "__main__":
    app.run(debug=True)