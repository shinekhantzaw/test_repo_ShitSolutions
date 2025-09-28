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

### 3.1) Create user and database:
**Linux/Mac:**
```bash
sudo -u postgres psql
```

**Windows:**
Open **SQL Shell (psql)** from Start Menu

Then run:
```sql
CREATE USER appuser WITH PASSWORD 'devpassword';
CREATE DATABASE appdb OWNER appuser;
GRANT ALL PRIVILEGES ON DATABASE appdb TO appuser;
```

### 3.2) Test the connection:
Run:
```bash
psql -h localhost -U appuser -d appdb -W
```

Enter password: `devpassword`  
If correct, you will see:
```
appdb=>
```
Exit with:
```sql
\q
```

### 3.3) Start and check database service:
**Linux/Mac:**
```bash
sudo systemctl start postgresql
sudo systemctl status postgresql
# Stop / Restart if needed
sudo systemctl stop postgresql
sudo systemctl restart postgresql
```

**Windows (Command Prompt as Administrator):**
```powershell
net start postgresql-x64-15
net stop postgresql-x64-15
```

**Windows (PowerShell as Administrator):**
```powershell
Start-Service postgresql-x64-15
Stop-Service postgresql-x64-15
Get-Service postgresql-x64-15   # Check status
```

### 3.4) Connecting with DBeaver DBMS:
Toolbar → Database → Connect to a database → select **PostgreSQL**  
Fill in setup information (user, password, db name, port) → Finish  

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