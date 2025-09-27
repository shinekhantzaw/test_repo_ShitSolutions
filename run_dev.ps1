# This PowerShell script will only work on Windows systems.

# Start database
Start-Service postgresql-x64-16

# Start backend
cd backend
.\.venv\Scripts\Activate.ps1
Start-Process -FilePath "python" -ArgumentList "-m uvicorn app.main:app --reload --port 8000"
cd ..

# Start frontend
cd frontend
Start-Process -FilePath "npm" -ArgumentList "run dev"
cd ..

# Info
Write-Output "Backend running at http://127.0.0.1:8000"
Write-Output "Frontend running at http://localhost:5173"

# Keep window open
Write-Output "Press Ctrl+C to stop processes."
Wait-Process -Name "python", "node"
