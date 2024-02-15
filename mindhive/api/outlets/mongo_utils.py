from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGO_CONNECTION_STRING)

db = client['mind-hive']

def fetch_all_outlets():
    outlets_collection = db['outlets']  # Access the collection
    return list(outlets_collection.find())  # Fetch all documents and convert cursor to list

