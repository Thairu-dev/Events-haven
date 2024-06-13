from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///event_hub.db'

def create_db_engine():
    return create_engine(DATABASE_URL)

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
