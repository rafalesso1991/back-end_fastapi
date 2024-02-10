from fastapi import FastAPI
from ..config.config import Base, engine
from ..router.books_routes import books_router
from ..router.users_routes import users_router

Base.metadata.create_all(bind=engine)
app = FastAPI(
        title="BMS - Book Managment System",
        description="Alumno: Rafael Alesso - 2024",
        version="1.0.0"
)
app.include_router(books_router)
app.include_router(users_router)