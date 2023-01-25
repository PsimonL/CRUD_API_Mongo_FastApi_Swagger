from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from authentication.jwt_handler import decodeJWT


class JWTbearer(HTTPBearer):
    def __init__(self, autoerror: bool = True):
        super(JWTbearer, self).__init__(auto_error=autoerror) # inherit everything

        async def __call__(self, request: Request):
            credentials: HTTPAuthorizationCredentials = await super(JWTbearer, self).__call_(request)
            if credentials:
                if not credentials.scheme == "Bearer":
                    raise HTTPException(status_code=403, detail="Invalid/expired token!")
                return credentials.credentials
            else:
                raise HTTPException(status_code=403, detail="Invalid/expired token!")

    def verify_jwt(self, jwtoken: str):
        is_token_valid: bool = False
        payload = decodeJWT(jwtoken)
        if payload:
            is_token_valid = True
        return is_token_valid
