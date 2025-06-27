from pymongo import MongoClient

def get_database():
    # Replace with your MongoDB URI (local or Atlas)
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client["applicationDB"]

def get_collection():
    db = get_database()
    return db["applications"]
