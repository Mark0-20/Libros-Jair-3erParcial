from config.database import Base
from sqlalchemy import Column, Integer, String

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor = Column(String)
    año = Column(Integer)
    categoria = Column(String, index=True)
    numero_paginas = Column(Integer)
