from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")

# SQLAlchemy connection string
DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create session
def test_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True, "Connection successful"
    except SQLAlchemyError as e:
        return False, str(e)