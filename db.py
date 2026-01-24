
from pymongo import MongoClient
from app.config import MongoConfig


connection = MongoClient(MongoConfig.mongo_url)
db = connection[MongoConfig.mongo_db_name]

def expCol():
    col = db[MongoConfig.mongo_expense_col]
    return col

def userCol():
    col = db[MongoConfig.mongo_user_col]
    return col

