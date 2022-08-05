from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, request
from flask_cors import CORS

from .database.db import db
from .routes.main import main_routes

# load environment
load_dotenv

database_uri = environ.get('DATABASE_URL')

# Set up the app

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)

CORS(app)
db.app = app
db.init_app(app)

app.register_blueprint(main_routes)

## Main

if __name__ == "__main__":
    app.run(debug=True)