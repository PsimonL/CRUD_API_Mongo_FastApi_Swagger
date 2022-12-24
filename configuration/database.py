from pymongo import MongoClient


class DatabaseSetUp:
    def __init__(self, mongoClientURL, dbName, collectionName):
        self.client = MongoClient(mongoClientURL)
        self.database = self.client[dbName]
        self.collection = self.database[collectionName]


initializer = DatabaseSetUp(
    "Mongo_DB_URL",
    "Database_Name",
    "Collection_Name"
)
