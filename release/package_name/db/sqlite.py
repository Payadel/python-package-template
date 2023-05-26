import threading
from sqlalchemy import (Boolean, Column, DateTime, Integer, String,
                        create_engine, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create thread-local storage
local_storage = threading.local()

# SQLite's connection string (using a local file named 'database.db')
db_url = 'sqlite:///database.db'
engine = create_engine(db_url)

Base = declarative_base()

Session = sessionmaker(bind=engine)

def get_db_session():
    # Check if session already exists for this thread
    if not hasattr(local_storage, 'session'):
        # Create a new session for this thread
        local_storage.session = Session()
    return local_storage.session


class BaeEntity(Base):
    __abstract__ = True
    created_time = Column(DateTime, default=func.now(), nullable=False)
    updated_time = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)


class User(BaeEntity):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    registered = Column(Boolean)


Base.metadata.create_all(engine)
