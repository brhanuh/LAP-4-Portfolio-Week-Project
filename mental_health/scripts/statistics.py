from ..database.db import db
from ..models.entry import Entry
from sqlalchemy.sql.functions import func

def getTotalEntries():
    try:
        totalEntries = Entry.query.all()
        return totalEntries
    except:
        print("Error getting data from db")

def getAvarage(targetFeeling, level):
    if targetFeeling != " " or level != " ":
        try:
            feeling = getTargetData(targetFeeling)
            totalEntries = Entry.query.count()
            target = Entry.query.filter(feeling == level).count()
            totalAvarage = (target / totalEntries) * 100
            totalAvarage = round(totalAvarage,1)
            return totalAvarage
        except:
            print("error getiing avarage")
    else:
        print("one or more args are empty")

def getTargetData(targetFeeling):

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
            case "date_posted":
                return Entry.date_posted
            case "user":
                return Entry.user
            case "week":
                return Entry.week
            case "day":
                return Entry.day
            case "time":
                return Entry.time
            case _:
                return Entry.mood
    else:
        print("error arg empty")
        
def getTargetQuery(target, value):

    if target != " ":
        targetData = getTargetData(target)
        try:
            target = Entry.query.filter(targetData ==  value).all()
            return target
        except:
            print("problem retriving date from database")
    else:
        print("target is empty")

def getUserWeek(user, week):
    if user != " " or week !=" ":
        targetData = getTargetData('week')
        targetUser = getTargetData('user')
        try:
            target = Entry.query.filter(targetUser == user, targetData ==  week).all()
            return target
        except:
            print("problem retriving date from database")
    else:
        print("user or week is empty")


def getMostRecentFeeling(user):

    targetUser = getTargetData('user')
    
    result = Entry.query.filter(targetUser == user).order_by(Entry.id.desc()).first()

    return result

