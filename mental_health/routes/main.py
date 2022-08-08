from flask import Blueprint, request, render_template
from ..database.db import db, datetime
from ..models.user import User
from ..models.entry import Entry
from ..scripts.statistics import getTotalEntries, getAvarage, getTargetDate
from werkzeug import exceptions

main_routes = Blueprint("main", __name__)

@main_routes.route("/new_entry", methods=["POST"])
def new_entry():

    try:
        date = datetime.strftime(datetime.today(), "%d-%m-%Y")
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

        new_entry = Entry(date_posted=date, mood=mood, energy=energy,
        depression=depression, irritability=irritability, motivation=motivation,
        stress=stress, appetite=appetite, concentration=concentration, diet=diet,
        enter=enter, social=social)

        db.session.add(new_entry)
        db.session.commit()

        return "Created new entry"
    except:
        print("error occured")

@main_routes.route("/entries", methods=["GET"])
def get_all_entries():
    try:
        all_entries = Entry.query.all()
        return render_template("index.html", all_entries=all_entries)
    except:
        print("Was not possible to retreive all entries")

@main_routes.route("/entry/<date>", methods=["GET"])   # for now i retrieving specific date
def get_entry(date):
    try:
        entries = getTargetDate(date)
        return render_template("entriesdate.html", all_entries=entries)
    except:
        print("error occured when retriving specific date")

@main_routes.route("/stats", methods=["GET"])
def get_statistics():

    try:
        all_entries = getTotalEntries()
        totalAvarage = getAvarage("mood", 2)
        return render_template("statistics.html", all_entries=all_entries, avarage=totalAvarage)
    except:
        print("error getting requesting statistics")

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


