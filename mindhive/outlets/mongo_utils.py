from pymongo import MongoClient

# Setup MongoDB connection
client = MongoClient('localhost', 27017)
db = client['mind-hive']

def fetch_all_outlets():
    outlets_collection = db['outlets']  # Access the collection
    return list(outlets_collection.find())  # Fetch all documents and convert cursor to list