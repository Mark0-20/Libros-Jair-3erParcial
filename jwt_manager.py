from jwt import encode, decode, exceptions
from fastapi import HTTPException

def create_token(data: dict):
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    try:
        data = decode(token, key="my_secret_key", algorithms=["HS256"])
        return data
    except exceptions.DecodeError:
        raise HTTPException(status_code=403, detail="Token mal formado o inválido")
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expirado")
    except Exception:
        raise HTTPException(status_code=403, detail="Error al validar token")