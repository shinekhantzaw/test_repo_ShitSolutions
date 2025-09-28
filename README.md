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
- PowerShell (by Microsoft) VSCode extension

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

Follow the images bellow:

| | |
|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/e0f48515-aacf-4c41-bc9e-a0a64d130395" width="500"> | <img src="https://github.com/user-attachments/assets/9671d24b-03ac-4c71-8db0-20a4ac93c95e" width="500"> |
| <img src="https://github.com/user-attachments/assets/31e04ee8-dc43-4b34-aabf-7e7630b43340" width="500"> | <img src="https://github.com/user-attachments/assets/4561f866-7978-4af7-9be5-00736fa4abd8" width="500"> |
| <img src="https://github.com/user-attachments/assets/0c34b9e5-1350-4bf2-9082-be34192920df" width="500"> | <img src="https://github.com/user-attachments/assets/c54903c7-d687-4b06-8297-a9e72a256c7e" width="500"> |
| <img src="https://github.com/user-attachments/assets/107d54cc-0682-42e3-937a-9e5d2bafa009" width="500"> | <img src="https://github.com/user-attachments/assets/abe25e77-c0da-49bc-938e-db5e61539154" width="500"> |
| <img src="https://github.com/user-attachments/assets/c1ec403b-2c46-482e-bb77-6b5290e23c2c" width="500"> |




---

## 4) Running the project:
**Windows (VSCode terminal)**

All setups commands are included within the shell script file `(run.ps1)`; no additonal step needed.

Run:
```PowerShell
.\run.ps1
```
Or you can run the app with play button if you installed PowerShell (by Microsoft) VSCode extenion

## Access the project:
- Backend (API) → http://127.0.0.1:8000  
- Frontend (React app) → http://localhost:5173  

---

## 5) Stopping the project:
-  **Ctrl+C** in the VSCode terminal to stop frontend sever.
-  **Ctrl+C** in the PowerShell pop-up window to stop backend sever.
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
