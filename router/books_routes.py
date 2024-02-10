from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from config.config import get_db
from models.book_model import BookModel
from schemas.book_schema import CreateBook, Book

books_router = APIRouter()

users_router = SQLAlchemyCRUDRouter(
    schema=Book,
    create_schema=CreateBook,
    db_model=BookModel,
    db=get_db,
    prefix="/books",
    tags=["Books"]
)