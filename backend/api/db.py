import os
from dotenv import load_dotenv
load_dotenv()

from loguru import logger
from sqlmodel import SQLModel, create_engine, Session


def get_db_url():
    try:
        
        DATABASE_URL = os.getenv("DATABASE_URL")
        if DATABASE_URL:
            # Trigger the success message
            logger.success(f"'DATABASE_URL' fetched successfully!")
            return DATABASE_URL
        else:            
            raise ValueError()
        
    except ValueError:
        logger.exception("oops!...No Value found for 'DATABASE_URL', please check your env file.")
    
engine = create_engine(get_db_url())

def init_db():
    logger.info("Initializing DB")
    SQLModel.metadata.create_all(engine)
    logger.success("DB Initialiazed")
    
    
def get_session():
    with Session(engine) as session:
        yield session
    
