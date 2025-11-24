from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///my_store.db", echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass 