import json
from ..database.db import db, datetime

class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.String(200), nullable=False)
    mood = db.Column(db.Integer, nullable=False)
    energy = db.Column(db.Integer, nullable=False)
    depression = db.Column(db.Integer, nullable=False)
    irritability = db.Column(db.Integer, nullable=False)
    motivation = db.Column(db.Integer, nullable=False)
    stress = db.Column(db.Integer, nullable=False)
    appetite = db.Column(db.Integer, nullable=False)
    concentration = db.Column(db.Integer, nullable=False)
    diet = db.Column(db.String(200))
    enter = db.Column(db.String(200))
    social = db.Column(db.String(200))

    def __repr__(self):
        return 'Entry ' + str(self.id)

class EntryEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Entry):
            return {'date_posted' : o.date_posted, 'mood' : o.mood, 'energy' : o.energy,
            'depression' : o.depression, 'irritability' : o.irritability, 'motivation' : o.motivation,
            'stress' : o.stress, 'appetatite' : o.appetite, 'concentration' : o.concentration, 'diet' : o.diet,
            'enter' : o.enter, 'social' : o.social}

        return super().default(o)