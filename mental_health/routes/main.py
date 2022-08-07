from flask import Blueprint, request, render_template
from ..database.db import db
from ..models.user import User
from ..models.entry import Entry
from ..scripts.statistics import getTotalEntries, getAvarage
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

    mood = request.form["mood"]
    energy = request.form["energy"]
    depression = request.form["depression"]
    irritability = request.form["irritability"]
    motivation = request.form["motivation"]
    stress = request.form["stress"]
    appetite = request.form["appetite"]
    concentration = request.form["concentration"]
    diet = request.form["diet"]
    enter = request.form["enter"]
    social = request.form["social"]

    new_entry = Entry(mood=mood, energy=energy, depression=depression,
    irritability=irritability, motivation=motivation, stress=stress,
    appetite=appetite, concentration=concentration, diet=diet,
    enter=enter, social=social)

    db.session.add(new_entry)
    db.session.commit()

    return "Created new entry"

@main_routes.route("/entries", methods=["GET"])
def get_all_entries():

    all_entries = Entry.query.all()
    return render_template("index.html", all_entries=all_entries)

@main_routes.route("/entry/<int:id>", methods=["GET"])
def get_entry():
    return "getting specific entry from db "

@main_routes.route("/stats", methods=["GET"])
def get_statistics():

    all_entries = getTotalEntries()
    totalAvarage = getAvarage("mood", 2)
    return render_template("statistics.html", all_entries=all_entries, avarage=totalAvarage)

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


