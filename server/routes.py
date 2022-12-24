from fastapi import APIRouter
from bson import ObjectId

from configuration.database import initializer

from model.model import DataTemplate
from configuration.schemas import SerializerForSingleObj, SerializerForMultipleObjs

router = APIRouter()


def return_func(x):
    return {"status": "WORKED", "json": x}


@router.get("/GetAll")
async def get_all():
    multiple_data = SerializerForMultipleObjs(initializer.collection.find())
    return return_func(multiple_data)


@router.get("/Get/{id}")
async def get_certain(id: str):
    single_data = SerializerForMultipleObjs(initializer.collection.find({"_id": ObjectId(id)}))
    return return_func(single_data)


@router.post("/SinglePost")
async def single_post(data: DataTemplate):
    _id = initializer.collection.insert_one(dict(data))
    single_data = SerializerForMultipleObjs(initializer.collection.find({"_id": _id.inserted_id}))
    return return_func(single_data)


@router.put("/SingleUpdate/{id}")
async def single_update(id: str, data: DataTemplate):
    initializer.collection.update_one({"_id": ObjectId(id)}, {"$set": dict(data)})
    single_data = initializer.collection.find({"_id": ObjectId(id)})
    return return_func(single_data)


@router.delete("/SingleDelete/{id}")
async def single_delete(id: str):
    initializer.collection.delete_one({"_id": ObjectId(id)})
    return return_func([])


@router.get("/")
async def get():
    return "Hello World!"
