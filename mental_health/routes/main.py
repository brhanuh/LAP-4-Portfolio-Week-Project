from flask import Blueprint, request, render_template
from ..database.db import db

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET"])
def index():
    return {"name": "Hello there"}