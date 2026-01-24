"""
Everything you need to do with the database of expense will be in this file.
Entire expense data CRUD operation will be executed here.
This file is not directly connected to the app.
"""
from db import db
from pymongo.errors import PyMongoError
from bson import ObjectId
from bson.errors import InvalidId

col = db.expCol()              #---> 'expenses' collection

def expenseCreate(expenseData: dict):
    try:
        result = col.insert_one(expenseData)
        return result.acknowledged
    except PyMongoError as e:
        print(f"Database failure while creating expense: {e}...\n")
        return False
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return False
    except Exception as e:
        print(f"Server failure while creating expense: {e}...\n")
        return False

def expenseRead(userID):
    #userID ---> type=ObjectID
    try:
        result = list(col.find({'userID':userID}, {'userID':0}))
        return result
    except PyMongoError as e:
        print(f"Database failure while reading expense data: {e}...\n")
        return False
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return False
    except Exception as e:
        print(f"Server failure while reading expense data: {e}...\n")
        return False

def expenseDelete(expenseID: str):
    #userID ---> type=str
    try:
        expenseID = ObjectId(expenseID)
        result = col.delete_one({'_id':expenseID})
        return result.deleted_count
    except PyMongoError as e:
        print(f"Database failure while deleting expense data: {e}...\n")
        return None
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return None
    except Exception as e:
        print(f"Server failure while deleting expense data: {e}...\n")
        return None

def expUpdate(expenseID: str, updateChoice: str, data):
    #expenseID ---> type = str
    try:
        expenseID = ObjectId(expenseID)
        filterQuery = {'_id': expenseID}
        if updateChoice == '1':
            updateQuery = {"$set":{"description": data}}
            result=col.update_one(filterQuery, updateQuery)
            if result.matched_count == 0:
                return None
            elif result.matched_count == 1:
                return result.modified_count
        elif updateChoice == '2':
            updateQuery = {"$set":{"amount": data}}
            result = col.update_one(filterQuery, updateQuery)
            if result.matched_count == 0:
                return None
            elif result.matched_count == 1:
                return result.modified_count
        elif updateChoice == '3':
            updateQuery = {"$set":{"date": data}}
            result = col.update_one(filterQuery, updateQuery)
            if result.matched_count == 0:
                return None
            elif result.matched_count == 1:
                return result.modified_count
    except PyMongoError as e:
        print(f"Database failure while updating description: {e}...\n")
        return None
    except InvalidId as e:
        print(f"Database failure due to invalid id: {e}...\n")
        return None
    except Exception as e:
        print(f"Server failure while updating description: {e}...\n")
        return None
