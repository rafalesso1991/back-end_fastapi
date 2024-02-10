from fastapi import APIRouter, Depends, HTTPException
from config.config import get_db
from models.book_model import BookModel
from schemas.book_schema import CreateBook, Book

books_router = APIRouter(
    tags=["Books"]
)
@books_router.get("/books/")
async def get_books(db=Depends(get_db)):
        books = db.query(BookModel).all()
        return books
@books_router.post("/books/", status_code=201, response_model=Book)
async def create_book(new_book: CreateBook, db=Depends(get_db)):
        book = BookModel(**new_book.model_dump())#dict method is deprecated in class BaseModel
        db.add(book)
        db.commit()
        db.refresh(book)
        return book
books_router.put("/books/{book_title}", response_model=Book)
async def update_book(book_id: int, updated_book: CreateBook, db=Depends(get_db)):
        book = db.query(BookModel).filter(BookModel.id == book_id).first()
        if not book:
                raise HTTPException(status_code=404, detail="Book not found")
        book.name = updated_book.name
        book.desc = updated_book.desc
        book.ownner_id = updated_book.owner_id
        db.commit()
        db.refresh(book)
        return book
books_router.delete("/books/{book_title}")
async def update_book(book_id: int, updated_book: CreateBook, db=Depends(get_db)):
        book = db.query(BookModel).filter(BookModel.id == book_id).first()
        if not book:
                raise HTTPException(status_code=404, detail="Book not found")
        db.delete(book)
        db.commit()
        return {"message": "Book deleted successfully"}