from ..database.db import db
from ..models.entry import Entry

def getTotalEntries():
    totalEntries = Entry.query.all()
    return totalEntries

def getAvarage(targetFeeling, level):

    feeling = getTargetFeeling(targetFeeling)
    totalEntries = Entry.query.count()
    target = Entry.query.filter(feeling == level).count()
    totalAvarage = (target / totalEntries) * 100
    totalAvarage = round(totalAvarage,1)
    return totalAvarage

def getTargetFeeling(targetFeeling):

    match targetFeeling:
        case "mood":
            return Entry.mood
        case "energy":
            return Entry.energy
        case "depression":
            return Entry.depression
        case "irritability":
            return Entry.irritability
        case "motivation":
            return Entry.motivation
        case "stress":
            return Entry.stress
        case "appetite":
            return Entry.appetite
        case "concentration":
            return Entry.concentration
        case "diet":
            return Entry.diet
        case "enter":
            return Entry.enter
        case "social":
            return Entry.social
        case _:
            return Entry.mood
        



