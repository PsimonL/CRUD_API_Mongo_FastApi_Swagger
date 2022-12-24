import json
import uvicorn as uvicorn
from fastapi import *
from pymongo import MongoClient

import server.routes

app = FastAPI()
app.include_router(server.routes.router)

if __name__ == "__main__":
    # uvicorn.run("server.routes:router", port=8080, reload=True)
    uvicorn.run("main:app", port=8080, reload=True)