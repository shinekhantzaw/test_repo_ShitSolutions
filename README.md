                                        Onboarding
--------------------------------------------------------------------------------------
1) Make sure you have these installed:
        Python 3.10+
        Node.js and npm
        PostgreSQL (running locally)
        Dbeaver DBMS for making alot of changes into the database
        SQLTools vscode extention (by Matheus Teixeira) for making light changes
        React Native Tools vscode extention
        ES7 React/Redux/GraphQL/React-Native snippets vscode extention
        Python Environments vscode extention

2) Clone the project

3) Database setup:
        We will all use the same setup so it’s simple for everyone:
        Username: appuser
        Password: devpassword
        Database: appdb
        Port: 5432

        Note: To keep things simple, let’s all use the same setup.
        That way no one needs a custom .env file for local development.
            
        3.1) Create user and database:
                On Linux/Mac:
                    sudo -u postgres psql
                On Windows:
                    Open SQL Shell (psql) from Start Menu

                Then run:
                    CREATE USER appuser WITH PASSWORD 'devpassword';
                    CREATE DATABASE appdb OWNER appuser;
                    GRANT ALL PRIVILEGES ON DATABASE appdb TO appuser;
            
        3.2) Test the connection:
                Run:
                    psql -h localhost -U appuser -d appdb -W
                Enter password: devpassword
                If correct, you will see:
                    appdb=>
                Exit with:
                    \q

        3.3) Start and check database service:
                Linux/Mac:
                    sudo systemctl start postgresql
                    sudo systemctl status postgresql
                    # Stop / Restart if needed:
                    sudo systemctl stop postgresql
                    sudo systemctl restart postgresql

                Windows (Command Prompt as Administrator):
                    net start postgresql-x64-15
                    net stop postgresql-x64-15

                Windows (PowerShell as Administrator):
                    Start-Service postgresql-x64-15
                    Stop-Service postgresql-x64-15
                    Get-Service postgresql-x64-15   # Check status

        3.4) Connecting with DBeaver DBMS:
                Toolbar > Database > Connect to a database > select: PostgreSQL
                Fill in setup information (user, password, db name, port) > Finish

4) Setup backend:
        cd backend
        python -m venv .venv
        source .venv/bin/activate   # On Linux/Mac
        .\.venv\Scripts\activate    # On Windows
        pip install -r requirements.txt

5) Setup frontend:
        cd frontend
        npm install

Running the project:
    Linux or Mac use run_dev.sh     ./run_dev.sh
    Windows use run_dev.ps1         .\run_dev.ps1

Access the project:
    Backend (API)           →   http://127.0.0.1:8000
    Frontend (React app)    →   http://localhost:5173

Stopping the project:
    On Linux/Mac press Ctrl+C in the terminal.
    On Windows close the PowerShell window or press Ctrl+C.
    Stop PostgreSQL if you don’t want to waste system resources:
        Linux/Mac   sudo systemctl stop postgresql

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
├── run_dev.sh           # Start backend + frontend (Linux/macOS)
└── run_dev.ps1          # Start backend + frontend (Windows)

