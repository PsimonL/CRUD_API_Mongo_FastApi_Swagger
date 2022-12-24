def SerializerForSingleObj(thing) -> dict:
    return {
        "id": str(thing["_id"]),
        "country": thing["country"],
        "city": thing["city"],
        "name": thing["name"],
        "net_worth": thing["net_worth"]
    }

def SerializerForMultipleObjs(thing) -> list:
    return [SerializerForSingleObj(it) for it in thing]