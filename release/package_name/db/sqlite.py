import threading

from sqlalchemy import (Boolean, Column, DateTime, Integer, String,
                        create_engine, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# Create thread-local storage
_local_storage = threading.local()

# SQLite's connection string (using a local file named 'database.db')
_db_url = 'sqlite:///database.db'
_engine = create_engine(_db_url)

Base = declarative_base()

_Session = sessionmaker(bind=_engine)


def get_db_session() -> Session:
    # Check if session already exists for this thread
    if not hasattr(_local_storage, 'session'):
        # Create a new session for this thread
        _local_storage.session = _Session()
    return _local_storage.session


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


Base.metadata.create_all(_engine)
