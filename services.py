from models import Book                 # SQLAlchemy Book model (DB table mapping)
from sqlalchemy.orm import Session     # Database session for queries/transactions
from schemas import BookCreate         # Pydantic schema for input validation

# CREATE operation: Add a new book to the database
def create_book(db: Session, data: BookCreate):
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

# READ operation: Get all books
def get_books(db: Session):
    return db.query(Book).all()   # Query all rows from books table

# READ operation: Get a single book by ID
def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

# UPDATE operation: Update an existing book
def update_book(db: Session, book: BookCreate, book_id: int):
    # Find the book in the database
    book_queryset = db.query(Book).filter(Book.id == book_id).first()
    if book_queryset:
        # Update fields dynamically from Pydantic data
        for key, value in book.model_dump().items():
            setattr(book_queryset, key, value)
        db.commit()
        db.refresh(book_queryset)
    return book_queryset

# DELETE operation: Remove a book from the database
def delete_book(db: Session, id: int):
    # Find book by ID
    book_queryset = db.query(Book).filter(Book.id == id).first()
    if book_queryset:
        db.delete(book_queryset)  # Mark book for deletion
        db.commit()                # Apply deletion
    return book_queryset


