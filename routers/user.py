from jwt_manager import create_token
from schemas.user import User
from fastapi import APIRouter
from fastapi.responses import JSONResponse

user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "max@gmail.com" and user.password == "maxi":
        token = create_token(user.model_dump())
        return JSONResponse(status_code=200, content={"access_token": token})
    return JSONResponse(status_code=401, content={"message": "Usuario o contraseña incorrectos"})
