from model.libro import Libro as LibroModel

class LibroService:
    def __init__(self, db):
        self.db = db

    def get_libros(self):
        return self.db.query(LibroModel).all()

    def get_libro_by_id(self, libro_id: int):
        return self.db.query(LibroModel).filter(LibroModel.id == libro_id).first()

    def get_libros_by_categoria(self, categoria: str):
        return self.db.query(LibroModel).filter(LibroModel.categoria == categoria).all()

    def create_libro(self, libro_data):
        new_libro = LibroModel(**libro_data)
        self.db.add(new_libro)
        self.db.commit()
        self.db.refresh(new_libro)
        return new_libro

    def update_libro(self, libro_id: int, libro_data):
        libro = self.get_libro_by_id(libro_id)
        if libro:
            for key, value in libro_data.items():
                setattr(libro, key, value)
            self.db.commit()
            self.db.refresh(libro)
            return libro
        return None

    def delete_libro(self, libro_id: int):
        libro = self.get_libro_by_id(libro_id)
        if libro:
            self.db.delete(libro)
            self.db.commit()
            return True
        return False