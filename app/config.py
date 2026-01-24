
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class MongoConfig:
    """This is configuration for mongodb connection"""
    mongo_url = getenv('MONGO_URL')
    mongo_db_name = getenv('MONGO_DB_NAME')
    mongo_user_col = getenv('MONGO_USER_COL')
    mongo_expense_col = getenv('MONGO_EXPENSE_COL')
