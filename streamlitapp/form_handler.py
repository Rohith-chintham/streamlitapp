from database import get_collection

def submit_application(data):
    collection = get_collection()
    collection.insert_one(data)
    return True
