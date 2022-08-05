from ..database.db import db, datetime

class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mood = db.Column(db.Integer, nullable=False)
    energy = db.Column(db.Integer, nullable=False)
    depression = db.Column(db.Integer, nullable=False)
    irritability = db.Column(db.Integer, nullable=False)
    motivation = db.Column(db.Integer, nullable=False)
    stress = db.Column(db.Integer, nullable=False)
    appetite = db.Column(db.Integer, nullable=False)
    concentration = db.Column(db.Integer, nullable=False)
    diet = db.Column(db.String(200))
    enterteinment = db.Column(db.String(200))
    social = db.Column(db.String(200))

