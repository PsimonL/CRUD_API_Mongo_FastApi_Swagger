from fastapi import APIRouter
from bson import ObjectId
from configuration.database import collection

from model.model import DataTemplate
from configuration.schemas import SerializerForSingleObj, SerializerForMultipleObjs


router = APIRouter()


@router.get("/GetAll")
async def get_all():
    multiple_data = SerializerForMultipleObjs(collection.find())
    return {"status": "OK", "multiple_data": multiple_data}
@router.get("/Get/{id}")
async def get_certain(id: str):
    single_data = SerializerForMultipleObjs(collection.find({"_id": ObjectId(id)}))
    return {"status": "OK", "single_data": single_data}

@router.post("/SinglePost")
async def single_post(data: DataTemplate):
    _id = collection.insert_one(dict(data))
    single_data = SerializerForMultipleObjs(collection.find({"_id": _id.inserted_id}))
    return {"status": "OK", "single_data": single_data}

# @router.put("/SingleUpdate/{id}")
# async def single_update(id: str, data: DataTemplate):
#     collection.find_one_and_update({"_id": ObjectId(id)}, {
#         "$set": dict(data)
#     })
#     return todos_serializer(collection.find({"_id": ObjectId(id)}))
#
# @router.delete("/SingleDelete/{id}")
# async def single_delete(id: str):
#     collection.find_one_and_delete({"_id": ObjectId(id)})
#     return {"status": "ok"}



@router.get("/HelloWorld")
async def get():
    return "Hello World!"
