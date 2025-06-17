from pydantic import BaseModel

class LibroBase(BaseModel):
    titulo: str
    autor: str
    año: int
    categoria: str
    numero_paginas: int

class Config:
    json_schema_extra = {
        "example": {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "año": 1967,
            "categoria": "Ficción",
            "numero_paginas": 417
        }
    }