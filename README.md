# Onboarding


## Collaboration Guidelines

- 🌿 Each collaborator must work on **their own branch**.  
- 🚀 Commit and push changes, then **create a Pull Request (PR)** for review.  
- 👥 Add **all teammates and the project advisor** as reviewers.  
- ✅ A PR will only be merged into `main` after **everyone approves** it.  
- 📝 **Document your code clearly** for team understanding.  
- 🧩 Follow a **modular and component-based structure** for better organization.  
- 🚫 Use `.gitignore` to avoid pushing unnecessary files to the repository.

---
## 1) Make sure you have these installed:
- **Python 3.10+**  
- **Node.js** and **npm**  
- **PostgreSQL** (running locally)  
- **pgAdmin 4** (Database Management Tool)  
- **VS Code Extensions:**
  - SQLTools (by Matheus Teixeira)
  - React Native Tools
  - ES7 React/Redux/GraphQL/React-Native snippets
  - Python Environments
  - PowerShell (by Microsoft)

---


## 2) Clone the project

Clone the repository to your local machine:

```PowerShell
git clone https://github.com/AdjudicatorMe/Senior-Capstone-Project.git
```
---

## 3) Database setup:
Follow the images below to install **PostgreSQL:**

| | |
|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/e0f48515-aacf-4c41-bc9e-a0a64d130395" width="500"> | <img src="https://github.com/user-attachments/assets/9671d24b-03ac-4c71-8db0-20a4ac93c95e" width="500"> |
| <img src="https://github.com/user-attachments/assets/31e04ee8-dc43-4b34-aabf-7e7630b43340" width="500"> | <img src="https://github.com/user-attachments/assets/4561f866-7978-4af7-9be5-00736fa4abd8" width="500"> |
| <img src="https://github.com/user-attachments/assets/0c34b9e5-1350-4bf2-9082-be34192920df" width="500"> | <img src="https://github.com/user-attachments/assets/c54903c7-d687-4b06-8297-a9e72a256c7e" width="500"> |
| <img src="https://github.com/user-attachments/assets/107d54cc-0682-42e3-937a-9e5d2bafa009" width="500"> | <img src="https://github.com/user-attachments/assets/abe25e77-c0da-49bc-938e-db5e61539154" width="500"> |
| <img src="https://github.com/user-attachments/assets/c1ec403b-2c46-482e-bb77-6b5290e23c2c" width="500"> | |

Create a `.env` file inside the **backend** folder to set up your database URL.  
Refer to `.env_example` for guidance.

---

## 4) Running the project

### **Windows (VS Code Terminal)**

If you stopped PostgreSQL previously, make sure to start it again:

```cmd
net start postgresql-x64-18
```

All setup commands are included in the PowerShell scripts; no extra steps are needed.

Run one of the following:

```powershell
run_backend.ps1     # Start backend (FastAPI)
run_frontend.ps1    # Start frontend (React/Vite)
run_fullstack.ps1   # Start both backend + frontend
run_DB.ps1          # Manage database (create/drop/seed)
```

> 💡 **Tip:**  
> If you have the **PowerShell (by Microsoft)** extension installed in VS Code, you’ll see a ▶️ play button above each script for easy execution.

---

## Access the project:
- Backend (API)             →           http://127.0.0.1:8000  
- Frontend (React app)      →           http://localhost:5173  

---

## **6) Stopping the Program**

- Press **Ctrl + C** in the VS Code terminal to stop the frontend server.  
- Press **Ctrl + C** in the PowerShell window to stop the backend server.  
- To stop PostgreSQL and save system resources:

```cmd
net stop postgresql-x64-18
```

