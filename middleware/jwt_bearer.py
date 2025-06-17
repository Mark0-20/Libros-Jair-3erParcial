from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        print("TOKEN recibido:", auth.credentials) 
        data = validate_token(auth.credentials)
        print("Datos decodificados del token:", data)
        if data["email"] != "max@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales no válidas")
        return data
