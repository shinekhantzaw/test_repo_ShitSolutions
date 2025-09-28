# Onboarding
---

## 1) Make sure you have these installed:
- Python 3.10+  
- Node.js and npm  
- PostgreSQL (running locally)  
- pgAdmin 4 DBMS
- SQLTools VSCode extension (by Matheus Teixeira) for making light changes  
- React Native Tools VSCode extension  
- ES7 React/Redux/GraphQL/React-Native snippets VSCode extension  
- Python Environments VSCode extension  

---

## 2) Clone the project

---

## 3) Database setup:
We will all use the same setup so it’s simple for everyone:

- **Username:** postgres  
- **Password:** capstone  
- **Database:** postgres  
- **Port:** 5432  

**Note:** To keep things simple, let’s all use the same setup.  
That way no one needs a custom `.env` file for local development.

---

## 4) Running the project:
**Windows**
```PowerShell
.\run.ps1
```
Or you can run the app with play button if you installed PowerShell (by Microsoft) VSCode extention

## Access the project:
- Backend (API) → http://127.0.0.1:8000  
- Frontend (React app) → http://localhost:5173  

---

## 5) Stopping the project:
-  **Ctrl+C** in the terminal.   
- Stop PostgreSQL if you don’t want to waste system resources:  

---

## Project Structure
```
test-app/
├── backend/             # FastAPI backend
│   ├── app/             # Application code
│   │   ├── db.py        # Database connection
│   │   ├── models.py    # Database models
│   │   ├── main.py      # FastAPI app (routes)
│   │   └── seed.py      # Optional: seeding helper
│   └── .venv/           # Virtual environment (local only)
│
├── frontend/            # React frontend (Vite)
│   ├── src/
│   │   ├── App.jsx      # Main entry
│   │   └── Input.jsx    # Student form + list
│   └── package.json
│
└── run.ps1              # Initialize and run the app (Windows only)
```