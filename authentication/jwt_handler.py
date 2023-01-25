import jwt
import time
import decouple

JWT_SECRET = decouple.config("secret")
JWT_ALGORITHM = decouple.config("algorithm")


# Returns generated JWT tokens
def token_response(token: str):
    return {"access_token": token}


def signJWT(user_id: str) -> dict[str, str]:
    payload = {"user_id": user_id, "expires": time.time() + 1200}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}