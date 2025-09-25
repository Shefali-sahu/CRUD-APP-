from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Database connection URL for PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/bookstore"

# Create an engine object that manages the connection to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory that will generate new Session objects
# - autocommit=False → transactions are committed manually
# - autoflush=False → changes are not automatically flushed to the database
# - bind=engine → session will be connected to our engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for all database models
# All ORM models will inherit from this Base
Base = declarative_base()

# Dependency to get DB session
def get_db():
    """
    Dependency function to provide a database session.
    - Opens a session when requested
    - Yields the session to be used inside a route
    - Ensures session is closed after request is finished
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create tables
def create_table():
    """  Creates all tables defined in ORM models (that inherit from Base).
    Equivalent to running CREATE TABLE statements in the database.  """
    Base.metadata.create_all(bind=engine)
