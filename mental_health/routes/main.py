import json
from flask import Blueprint, request, render_template, jsonify
from ..database.db import db, datetime
from ..models.user import User
from ..models.entry import Entry, EntryEncoder
from ..scripts.statistics import getTargetQuery, getTotalEntries, getAvarage, getUserWeek
from werkzeug import exceptions
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask_jwt_extended import jwt_required

main_routes = Blueprint("main", __name__)

@main_routes.route("/new_entry", methods=["POST"])
@jwt_required()
def new_entry():

    
    try:
        user = get_jwt_identity()
        data = request.get_json()
        date = datetime.strftime(datetime.today(), "%d-%m-%Y")
        day = datetime.strftime(datetime.today(), "%A")
        week = datetime.strftime(datetime.today(), "%W")
        time = datetime.strftime(datetime.today(), "%H-%M")
        mood = data["mood"]
        energy = data["energy"]
        depression = data["depression"]
        irritability = data["irritability"]
        motivation = data["motivation"]
        stress = data["stress"]
        appetite = data["appetite"]
        concentration = data["concentration"]
        diet = data["diet"]
        enter = data["enter"]
        social = data["social"]

        new_entry = Entry(user=user, date_posted=date,
        day=day, week=week, time=time, mood=mood, energy=energy, depression=depression, irritability=irritability, motivation=motivation,
        stress=stress, appetite=appetite, concentration=concentration, diet=diet,
        enter=enter, social=social)

        db.session.add(new_entry)
        db.session.commit()

        return "Created new entry", 200
    except:
        print("error occured")

@main_routes.route("/entries", methods=["GET"])
@jwt_required()
def get_all_entries():
    try:

        all_entries = getTotalEntries()
        jsonified_d = json.dumps(all_entries, cls=EntryEncoder, indent=4)
        return jsonified_d , 200
        
    except:
        print("Was not possible to retreive all entries")

@main_routes.route("/entry/<target>/<value>", methods=["GET"])   # for now i retrieving specific target
def get_entry(target, value):
    try:
        entries = getTargetQuery(target,value)
        jsonified_d = json.dumps(entries, cls=EntryEncoder, indent=4)
        return jsonified_d
    except:
        print("error occured when retriving specific date")

@main_routes.route("/stats/<target>/<value>", methods=["GET"])
@jwt_required()
def get_statistics(target, value):

    try:
        totalAvarage = getAvarage(target, value)
        jsonified_d = f'{{"level of {target} " : {value}, " total" : {totalAvarage}}}'
        return jsonified_d
    except:
        print("error getting requesting statistics")

@main_routes.route("/week_stats/<target>", methods=["GET"])
@jwt_required()
def get_user_week(target):

    try:
        week = datetime.strftime(datetime.today(), "%W")
        week_entries = getUserWeek(target, week)
        jsonified_d = json.dumps(week_entries, cls=EntryEncoder, indent=4)
        return jsonified_d
    except:
        print("error getting requesting statistics")


@main_routes.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@main_routes.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@main_routes.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"SERVER ERROR,  {err}"}, 500





@main_routes.route('/profile')
@jwt_required()
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body  



      


    # day=day, week=week, time=time,
