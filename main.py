import json

import uvicorn as uvicorn
from fastapi import *
from pymongo import MongoClient

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8080, reload=True)
