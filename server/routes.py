import json
from fastapi import APIRouter, Body, Depends
from bson import ObjectId

from configuration.database import initializer
from configuration.model import PostFilmSchema, UserSchema, UserLoginSchema
from configuration.serializers import FilmEntity, EntitySerializerFilm, UserEntity, EntitySerializerUser, \
    EntitySerializerLoginUser
from authentication.jwt_handler import signJWT
from authentication.jwt_bearer import JWTbearer

router = APIRouter()


def return_func(x, message):
    return {"status": message, "json": x}


@router.get("/MultipleFilms", tags=["films"])
async def get_all() -> json:
    multiple_data = EntitySerializerFilm(initializer.collection.find())
    return return_func(multiple_data, "Returned Films")


@router.get("/Film/{id}", tags=["films"])
async def get_certain(id: str) -> json:
    single_data = FilmEntity(initializer.collection.find({"_id": ObjectId(id)}))
    return return_func(single_data, f"Get Film for id = {id}")


@router.post("/AddFilm", tags=["films"], dependencies=[Depends(JWTbearer())])
async def single_post(film: PostFilmSchema):
    _id = initializer.collection.insert_one(dict(film))
    single_data = FilmEntity(initializer.collection.find_one({"_id": _id.inserted_id}))
    return return_func(single_data, f"Post Film for id = {id}")


@router.put("/UpdateFilm/{id}", tags=["films"])
async def single_update(id: str, film: PostFilmSchema):
    initializer.collection.update_one({"_id": ObjectId(id)}, {"$set": dict(film)})
    single_data = FilmEntity(initializer.collection.find({"_id": ObjectId(id)}))
    return return_func(single_data, f"Update Film for id = {id}")


@router.delete("/DeleteFilm/{id}", tags=["films"])
async def single_delete(id: str):
    initializer.collection.delete_one({"_id": ObjectId(id)})
    return return_func({}, None)


@router.post("/user/signup", tags=["user"], dependencies=[Depends(JWTbearer())])
async def user_signup(user: UserSchema = Body(default=None)):
    _id = initializer.collection.insert_one(dict(user))
    data = EntitySerializerUser(initializer.collection.find({"_id": _id.inserted_id}))
    return signJWT(user.email)


def check_if_user_exists(validator: UserLoginSchema):
    users = EntitySerializerLoginUser(initializer.collection.find())
    for user in users:
        if user.get("password") == validator.password and user.get("email") == validator.email:
            return True
        else:
            return False


@router.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(default=None)):
    if check_if_user_exists(user):
        return signJWT(user.email)
    else:
        return {"ERROR": "Invalid login credentials!"}


@router.get("/me", tags=["CheckIfWorkingToken"], dependencies=[Depends(JWTbearer())])
async def get_me(user: UserSchema = Body(default=None)):
    return user


@router.get("/", tags=["CheckIfWorking"])
async def get():
    return "Hello World!"
