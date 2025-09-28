# import to read environment variables from the OS
import os
# import read .env file
from dotenv import load_dotenv
# import for the connection to the DB
from sqlalchemy import create_engine
# import for session and base class for ORM models
from sqlalchemy.orm import sessionmaker, declarative_base

# load_dotenv, create_engine, sessionmaker, declarative_base
# are from SQLAlchemy package which is installed via pip,
# inside the virtual environment(.venv)

#!!Do not push your .env file to GitHub!!

# read .env file
load_dotenv()

# set the database URL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:capstone@localhost:5432/postgres"
)

# engine is the connection to Postgres
# pool_pre_ping=True checks if the connection is alive
engine = create_engine(DATABASE_URL, pool_pre_ping=True) 

# session is how we talk to the DB
# autocommit=False means we have to call commit() to save changes
# autoflush=False means we have to call flush() to send changes to the DB
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


# Base is for ORM models
# ORM(Object Relational Mapping) maps Python classes to DB tables
Base = declarative_base()
