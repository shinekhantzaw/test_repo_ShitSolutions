# import necessary modules
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .db import SessionLocal
from .models import Student
from .seed import init_db

# initialize the database and insert data
init_db()

# create the FastAPI app
app = FastAPI()

# allow React dev server later (Vite uses 5173)
# Cross-Origin Resource Sharing, so your React(port 5173) app can call
# the backend (port 8000)
# This is how frontend and backend can talk to each other
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
# It's going to try to get a session, yield it, and then close it
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# notice the decorator for GET/POST request (@app.get or @app.post)
# These are what you see on CLI log example: INFO: Started server process [4043]
# Example: if you visit http://127.0.0.1:8000/health, you should see that JSON response.

# Basic health check, nothing to do with DB
@app.get("/health") 
def health():
    return {"status": "ok"}

# List students from the DB
@app.get("/students")
def list_students(db: Session = Depends(get_db)):
    rows = db.query(Student).order_by(Student.id).all()
    return [{"id": s.id, "name": s.name, "major": s.major, "year": s.year} for s in rows]

# Create a new student to post to the DB
class StudentCreate(BaseModel):
    name: str
    major: str | None = None
    year: int | None = None

# POST students
@app.post("/students", status_code=201)
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):
    s = Student(name=payload.name, major=payload.major, year=payload.year)
    db.add(s)
    db.commit()
    db.refresh(s)
    return {"id": s.id, "name": s.name, "major": s.major, "year": s.year}
