import json
import uvicorn as uvicorn
from fastapi import *
from pymongo import MongoClient
from fastapi import FastAPI
import connection
from bson import ObjectId

app = FastAPI()



# An instance of class User
newuser = Customer()

# funtion to create and assign values to the instanse of class Customer created
def create_user(email, username):
    newuser.cust_id = ObjectId()
    newuser.cust_email  = email
    newuser.cust_name = username
    return dict(newuser)

@app.get("/get", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

# @app.post("/post", tags=["Root"])
# def postFunc():