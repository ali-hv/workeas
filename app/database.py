from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Setup SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite3.db"

# Create engine and SessionLocal class
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the database
Base = declarative_base()

def get_db():
    # Create a database session
    db = SessionLocal()
    try:
        # Yield the database session
        yield db
    finally:
        # Close the database session
        db.close()