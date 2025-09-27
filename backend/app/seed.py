# import the session from db.py
from .db import SessionLocal
# import reset_db function from models.py
from .models import Student, reset_db

# function to initialize the database and seed data
def init_db():
    
    # Reset tables before seeding, if you want to keep existing data, comment this out
    reset_db()

    db = SessionLocal()
    # create sample students objects
    sample_students = [
        # call Student constructor to create objects
        Student(name="Shine", major="Computer Science", year=2026),
        Student(name="Alex", major="Math", year=2025),
    ]
    # add all sample students to the session
    db.add_all(sample_students)
    # commit to save to the database
    db.commit()
    # close the session
    db.close()
