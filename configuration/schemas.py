def SerializerForSingleObj(thing) -> dict:
    return {
        "id": str(thing["_id"]),
        "name": thing["name"],
        "counter": thing["counter"]
    }

def SerializerForMultipleObjs(thing) -> list:
    return [SerializerForSingleObj(it) for it in thing]