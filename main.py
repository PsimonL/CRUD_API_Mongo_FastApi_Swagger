import json
import uvicorn as uvicorn
from fastapi import *
from pymongo import MongoClient

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("server:app", port=8080, reload=True)
