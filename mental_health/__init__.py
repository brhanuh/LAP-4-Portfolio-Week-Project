from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, request
from datetime import timedelta
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from .models.user import User, Post


from flask_cors import CORS

from .database.db import db
from .routes.main import main_routes
from .routes.auth import auth_routes
from .routes.recommendation import recom_route

# load environment
load_dotenv()

database_uri = environ.get('DATABASE_URL')

if 'postgres:' in database_uri:
    database_uri = database_uri.replace("postgres:", "postgresql:")

# Set up the app

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "dakzbakz12345tok"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
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
app.register_blueprint(recom_route, url_prefix = '/recommendations')

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

## Main

if __name__ == "__main__":
    app.run(debug=True)