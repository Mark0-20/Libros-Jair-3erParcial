from middleware.cors import configure_cors
from fastapi import FastAPI
from middleware.error_handler import ErrorHandler
from routers.libro import libros_router
from config.database import engine, Base
from routers.user import user_router



app = FastAPI()

configure_cors(app)

app.add_middleware(ErrorHandler)
app.include_router(user_router)
app.include_router(libros_router)

Base.metadata.create_all(bind=engine)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Book API"}
