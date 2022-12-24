def EntityForSingleObject(thing) -> dict:
    return {
        "id": str(thing["_id"]),
        "name": thing["name"],
        "counter": thing["counter"]
    }

def EntityForMultipleObject(thing) -> list:
    return [EntityForSingleObject(it) for it in thing]