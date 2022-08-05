from flask import Blueprint, request, render_template
from ..database.db import db
from werkzeug import exceptions

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET"])
def index():
    return "Hello World"

@main_routes.route("/register", methods=["GET", "POST"])
def register():
    return "Registering"

@main_routes.route("/login", methods=["GET", "POST"])
def login():
    return "Login in"

@main_routes.route("/new_entry", methods=["POST"])
def new_entry():
    return "Creating new entry"

@main_routes.route("/entries", methods=["GET"])
def get_all_entries():
    return "getting all entries from db "

@main_routes.route("/entry/<int:id>", methods=["GET"])
def get_entry():
    return "getting specific entry from db "

@main_routes.route("/stats", methods=["GET"])
def get_statistics():
    return "get statistics about the users who are feeling same way as you"

@main_routes.route("/recommendations", methods=["GET"])
def get_recommendations():
    return "get recommendations from the users who are feeling same way as you"

@main_routes.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@main_routes.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@main_routes.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"SERVER ERROR,  {err}"}, 500


