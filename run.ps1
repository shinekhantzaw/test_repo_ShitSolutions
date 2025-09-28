
# Install powershell extension for VS Code for better experience.
# You can run the app with play button in VS Code or run the script directly in PowerShell terminal.

# Bypass execution policy for this script
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Backend setup
Write-Host ""
Write-Host "------------------ Starting backend ------------------" -ForegroundColor DarkMagenta
Write-Host ""
Set-Location "$PSScriptRoot\backend" # Change to backend directory
Write-Host "Current directory: $PWD" -ForegroundColor DarkYellow

# Create virtual environment if it doesn't exist
if (-Not (Test-Path ".\.venv")) {
    Write-Host "Creating virtual environment this may take a while..." -ForegroundColor Cyan
    python -m venv .venv 
    Write-Host "Virtual environment created." -ForegroundColor Cyan
}

# Activate virtual environment
.\.venv\Scripts\activate
Write-Host "Virtual environment activated." -ForegroundColor Cyan

# Install Python dependencies
pip install -r requirements.txt --quiet # --quiet hide the installation logs for cleaner output in terminal
Write-Host ""
Write-Host "Python dependencies from requirements.txt installed." -ForegroundColor Cyan

# Start backend server in background
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd `"$PWD`"; .\.venv\Scripts\activate; uvicorn app.main:app --reload --port 8000"
Write-Host "Backend Logs can be found in the new pop-up PowerShell." -ForegroundColor Cyan
Write-Host ""
Write-Host "Ctrl+C in power shell pop-up to stop the backend server." -ForegroundColor Cyan

Write-Host ""
Write-Host "Backend: http://localhost:8000" -ForegroundColor Green

Write-Host ""
Write-Host "------------------ Starting frontend ------------------" -ForegroundColor DarkMagenta
Write-Host ""
Set-Location "$PSScriptRoot\frontend"
Write-Host "Current directory: $PWD" -ForegroundColor DarkYellow

# Install Node dependencies
npm install
Write-Host ""
Write-Host "Node dependencies installed." -ForegroundColor Cyan
Write-Host ""
Write-Host "Ctrl+C in vs code terminal to stop the frontend server." -ForegroundColor Cyan
Write-Host ""

Write-Host "-------------------------------------------------------------" -ForegroundColor DarkMagenta
# Start frontend server
npm run dev

