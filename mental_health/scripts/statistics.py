from ..database.db import db
from ..models.entry import Entry

def getTotalEntries():
    try:
        totalEntries = Entry.query.all()
        return totalEntries
    except:
        print("Error getting data from db")

def getAvarage(targetFeeling, level):
    if targetFeeling != " " or level != " ":
        try:
            feeling = getTargetFeeling(targetFeeling)
            totalEntries = Entry.query.count()
            target = Entry.query.filter(feeling == level).count()
            totalAvarage = (target / totalEntries) * 100
            totalAvarage = round(totalAvarage,1)
            return totalAvarage
        except:
            print("error getiing avarage")
    else:
        print("one or more args are empty")

def getTargetFeeling(targetFeeling):

    if targetFeeling != " ":
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
    else:
        print("error arg empty")
        
def getTargetDate(targetDate):

    if targetDate != " ":
        try:
            target = Entry.query.filter(Entry.date_posted ==  targetDate ).all()
            return target
        except:
            print("problem retriving date from database")
    else:
        print("date is empty")

