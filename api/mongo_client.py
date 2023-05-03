import os
from pymongo import MongoClient  # Import MongoClient class from pymongo package
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")
# created enviroment for os.environ(dotenv use .env.local)

MONGO_URL = (os.environ.get("MONGO_URL", "mongo"),)
MONGO_USERNAME = (os.environ.get("MONGO_USERNAME", "root"),)
# Defined from .env.local
MONGO_PASSWORD = (os.environ.get("MONGO_PASSWORD", ""),)
# Defined from .env.local in case to be more safe (the same as in docker-compose file)
MONGO_PORT = (os.environ.get("MONGO_PORT", 27017),)

mongo_client = MongoClient(  # Created new instance of the MongoClient class
    host=MONGO_URL,  # Utilized parameter
    username=MONGO_USERNAME,  # Utilized parameter
    password=MONGO_PASSWORD,  # Utilized parameter
    port=MONGO_PORT,  # Utilized parameter
)


def insert_test_document():
    # after, when class above was created, made function and verify it in main.py
    db = mongo_client.test
    test_collection = db.test_collection
    res = test_collection.insert_one({"name": "Exiscute", "Student": True})
    print(res)
