import json
import uvicorn as uvicorn
from fastapi import *
from pymongo import MongoClient
from fastapi import APIRouter
import connection
from bson import ObjectId
from configuration.database import collection
from model.model import DataTemplate
from configuration.schemas import EntityForSingleObject, EntityForMultipleObject
from bson import ObjectId

router = APIRouter()


@router.get("/GetAll")
async def get_all():
    multiple_data = EntityForMultipleObject(collection.find())
    return {"status": "OK", "multiple_data": multiple_data}


@router.get(f"/Get/{id}")
async def get_certain(id: str):
    single_data = EntityForMultipleObject(collection.find({"_id": ObjectId(id)}))
    return {"status": "OK", "single_data": single_data}


@router.get("/HelloWorld")
async def get():
    return "Hello World!"
