#!/bin/bash

# This shell script will only work on Linux and MacOS systems.

# Start PostgreSQL service
sudo systemctl start postgresql

# Start backend in background
cd backend
source .venv/bin/activate
python -m uvicorn app.main:app --reload --port 8000 &
BACKEND_PID=$!
cd ..

# Start frontend in background
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Info
echo "Backend running at http://127.0.0.1:8000"
echo "Frontend running at http://localhost:5173"

# Wait for processes so script doesn't exit immediately
wait $BACKEND_PID $FRONTEND_PID
