import json
import os
from pymongo import MongoClient

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'MongoCredentials.json')


class DatabaseSetUp:
    def __init__(self, mongoClientURL, dbName, collectionName):
        self.client = MongoClient(mongoClientURL)
        self.database = self.client[dbName]
        self.collection = self.database[collectionName]


def db_helper(x):
    file = open(filename)
    data = json.load(file)
    file.close()
    return data.get(x)


initializer = DatabaseSetUp(
    f"mongodb+srv://{db_helper('username')}:{db_helper('password')}@cluster0.4ffgt.mongodb.net/?retryWrites=true&w=majority",
    db_helper('cluster'),
    db_helper('collection')
)

# try:
#     conn = initializer.server_info()
#     print(f'Connected to MongoDB {conn.get("version")}')
# except Exception:
#     print("Unable to connect to the MongoDB server.")
