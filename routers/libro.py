from fastapi import Path, Query, Depends, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session
from service.libro import LibroService
from schemas.libro import LibroBase
from middleware.jwt_bearer import JWTBearer
from model.libro import Libro as LibroModel

libros_router = APIRouter()

@libros_router.get('/libros/{libro_id}', tags=['Libros'], response_model=LibroBase, dependencies=[Depends(JWTBearer())])
def get_libro(libro_id: int = Path(ge=1)) -> LibroBase:
    db = Session()
    try:
        result = LibroService(db).get_libro_by_id(libro_id)
        if not result:
            return JSONResponse(status_code=404, content={"message": "Libro no encontrado"})
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    finally:
        db.close()

@libros_router.get('/libros', tags=['Libros'], response_model=List[LibroBase], dependencies=[Depends(JWTBearer())])
def get_libros() -> List[LibroBase]:
    db = Session()
    try:
        result = LibroService(db).get_libros()
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    finally:
        db.close()

@libros_router.get('/libros/categoria/{categoria}', tags=['Libros'], response_model=List[LibroBase], dependencies=[Depends(JWTBearer())])
def get_libros_by_categoria(categoria: str = Path(min_length=3, max_length=25)) -> List[LibroBase]:
    db = Session()
    try:
        result = LibroService(db).get_libros_by_categoria(categoria)
        if not result:
            return JSONResponse(status_code=404, content={"message": "No se encontraron libros en esa categoría"})
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    finally:
        db.close()

@libros_router.post('/libros', tags=['Libros'], status_code=201, dependencies=[Depends(JWTBearer())])
def create_libro(libro: LibroBase):
    db = Session()
    try:
        LibroService(db).create_libro(libro.model_dump())
        return {"message": "Libro registrado correctamente"}
    finally:
        db.close()

@libros_router.put('/libros/{libro_id}', tags=['Libros'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_libro(libro_id: int, libro: LibroBase) -> dict:
    db = Session()
    try:
        result = LibroService(db).get_libro_by_id(libro_id)
        if not result:
            return JSONResponse(status_code=404, content={"message": "Libro no encontrado"})
        LibroService(db).update_libro(libro_id, libro.model_dump())
        return JSONResponse(status_code=200, content={"message": "Libro actualizado correctamente"})
    finally:
        db.close()

@libros_router.delete('/libros/{libro_id}', tags=['Libros'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_libro(libro_id: int) -> dict:
    db = Session()
    try:
        result = db.query(LibroModel).filter(LibroModel.id == libro_id).first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "Libro no encontrado"})
        LibroService(db).delete_libro(libro_id)
        return JSONResponse(status_code=200, content={"message": "Libro eliminado correctamente"})
    finally:
        db.close()
 