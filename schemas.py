from pydantic import BaseModel

# Base schema (common fields for a Book)
class BookBase(BaseModel):
    title: str
    author: str
    description: str
    year: int

# Schema used when creating a new book
# (inherits all fields from BookBase, no 'id' yet)
class BookCreate(BookBase):
    pass

# Schema used when reading or returning a book from DB
# (extends BookBase and adds an 'id' field)
class Book(BookBase):
    id: int

    class Config:
        # orm_mode = True  # pydantic version < 2.x
        from_attributes = True  # pydantic version > 2.x
