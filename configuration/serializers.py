def wrapperFilm(func):
    def inner(*args, **kwargs):
        dictHelp = func(*args, **kwargs)
        return [itF for itF in dictHelp.items()]
    return inner


@wrapperFilm
def FilmEntity(film) -> dict:
    return {
        "id": str(film["_id"]),
        "film_name": film["film_name"],
        "author": film["author"],
        "production_year": film["production_year"],
        "film_length": film["film_length"],
        "when_to_watch": film["when_to_watch"],
        "film_description": film["film_description"]
    }


def UserEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullName": user["fullName"],
        "password": user["password"],
        "email": user["email"]
    }


def UserLoginEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "password": user["password"]
    }


# make decorator
def EntitySerializerFilm(film) -> list:
    return [FilmEntity(itF) for itF in film]


# make decorator
def EntitySerializerUser(user) -> list:
    return [UserEntity(itU) for itU in user]


# make decorator
def EntitySerializerLoginUser(login) -> list:
    return [UserLoginEntity(itL) for itL in login]
