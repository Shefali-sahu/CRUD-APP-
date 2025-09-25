from db import Base # Import the Base class (from SQLAlchemy's declarative_base)
from sqlalchemy import Integer, Column, String

# Define the Book model (represents a "books" table in the database)
class Book(Base):
    __tablename__ = "books"   # table name in database

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)
