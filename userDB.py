"""
Everything you need to do with the database of users will be in this file.
Entire user data CRUD operation will be executed here.
This file is not directly connected to the app.
"""

from db import db
from pymongo.errors import PyMongoError
from bson.errors import InvalidId

col = db.userCol()                 #---> 'users' collection

def passFetcher(userID):
    #userID ---> type = ObjectID
    try:
        result = col.find_one({"_id": userID}, {"password": 1})
        return result
    except PyMongoError as e:
        print(f"Database failure while creating user: {e}...\n")
        return False
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return False
    except Exception as e:
        print(f"Server failure while creating user: {e}...\n")
        return False

def userCreate(userData: dict):
    try:
        result = col.insert_one(userData)
        #print(result)                                  #Delete Later
        return result.acknowledged
    except PyMongoError as e:
        print(f"Database failure while creating user: {e}...\n")
        return False
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return False
    except Exception as e:
        print(f"Server failure while creating user: {e}...\n")
        return False

def userRead(userData: dict):
    try:
        result = col.find_one(userData)
        return result
    except PyMongoError as e:
        print(f"Database failure while reading user data: {e}...\n")
        return False
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return False
    except Exception as e:
        print(f"Server failure whilte creating user: {e}...\n")
        return False

def AccDetailRead(userID_dict: dict):
    try:
        result = col.find_one(userID_dict, {'_id':0, 'password':0})
        return result
    except PyMongoError as e:
        print(f"Database failure while reading user data: {e}...\n")
        return False
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return False
    except Exception as e:
        print(f"Server failure whilte creating user: {e}...\n")
        return False

def AccDetailUpdate(userID, accUpdateChoice: str, data: str):
    #userID --> type = ObjectID
    try:
        filerQuery = {"_id": userID}
        if accUpdateChoice== '1':
            updateQuery = {"$set":{"name": data}}
        elif accUpdateChoice == '2':
            updateQuery = {"$set": {"email": data}}
        elif accUpdateChoice == '3':
            updateQuery = {"$set": {"dateOfBirth": data}}
        elif accUpdateChoice == '4':
            updateQuery = {"$set": {"address": data}}
        elif accUpdateChoice == '5':
            updateQuery = {"$set": {"password": data}}
        result = col.update_one(filerQuery, updateQuery)
        if result.matched_count == 0:
            return None
        elif result.matched_count == 1:
            return result.modified_count
    except PyMongoError as e:
        print(f"Database failure while reading user data: {e}...\n")
        return None
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return None
    except Exception as e:
        print(f"Server failure whilte creating user: {e}...\n")
        return None

def AccDelete(userID):
    #userID ---> type = ObjectID
    try:
        result = col.delete_one({"_id": userID})
        return result.deleted_count
    except PyMongoError as e:
        print(f"Database failure while reading user data: {e}...\n")
        return None
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return None
    except Exception as e:
        print(f"Server failure whilte creating user: {e}...\n")
        return None
