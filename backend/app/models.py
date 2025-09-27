# import necessary modules
from sqlalchemy import Column, Integer, Text

# import Base and engine to create/reset tables
from .db import Base, engine

# Student class/model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    major = Column(Text)
    year = Column(Integer)

# Reset database function
def reset_db():
    # Drop all tables
    Base.metadata.drop_all(bind=engine)
    # Recreate all tables
    Base.metadata.create_all(bind=engine)

