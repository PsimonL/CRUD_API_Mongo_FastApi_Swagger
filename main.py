import json
from fastapi import *
from pymongo import MongoClient

client = MongoClient("")
database = client[""]
collection = database[""]

app = FastAPI()

app.

if __name__ == '__main__':
    app.run(debug=True, port=8080)
