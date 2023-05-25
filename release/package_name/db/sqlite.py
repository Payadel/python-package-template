from sqlalchemy import (Boolean, Column, DateTime, Integer, String,
                        create_engine, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite's connection string (using a local file named 'database.db')
db_url = 'sqlite:///database.db'
engine = create_engine(db_url)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


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
