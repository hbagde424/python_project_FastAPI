# 🚀 START HERE - Employee Management System

## Welcome! 👋

You have a complete, production-ready full-stack application. Let's get it running!

---

## ⚡ Quick Start (2 minutes)

### Step 1: Start Backend
Open Terminal 1 and run:
```bash
cd backend
python run.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 2: Start Frontend
Open Terminal 2 and run:
```bash
cd frontend
npm install  # First time only
npm run dev
```

You should see:
```
➜  Local:   http://localhost:3000/
```

### Step 3: Open Application
Click or visit: **http://localhost:3000**

---

## 📍 Important URLs

| What | URL |
|------|-----|
| **Frontend** | http://localhost:3000 |
| **Backend API** | http://localhost:8000/api/v1 |
| **API Documentation** | http://localhost:8000/docs |
| **Health Check** | http://localhost:8000/health |

---

## 🎯 What You Can Do

### On the Employees Page
- ✅ Create new employees
- ✅ View all employees
- ✅ Edit employee details
- ✅ Delete employees
- ✅ Navigate with pagination

### On the Dashboard
- ✅ View employee statistics
- ✅ See department breakdown
- ✅ View salary information

---

## 🧪 Test the Application

### Create an Employee
1. Click "Add Employee"
2. Fill in the form with sample data
3. Click "Create"
4. You should see a success message

### View Dashboard
1. Click "Dashboard" in the navigation
2. You should see statistics

---

## 🐛 Troubleshooting

### Backend Won't Start
```bash
cd backend
# Check if port 8000 is in use
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows
```

### Frontend Won't Start
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### API Connection Error
1. Make sure backend is running: `cd backend && python run.py`
2. Check API URL in `frontend/src/api/client.js`
3. Check browser console (F12) for errors

---

## 📚 Documentation

- **[README.md](README.md)** - Main project documentation
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick commands
- **[RUN_FULL_STACK.md](RUN_FULL_STACK.md)** - Detailed setup
- **[INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)** - How it works
- **[backend/README.md](backend/README.md)** - Backend docs
- **[frontend/README.md](frontend/README.md)** - Frontend docs

---

## 🎊 You're All Set!

**Terminal 1:**
```bash
cd backend
python run.py
```

**Terminal 2:**
```bash
cd frontend
npm run dev
```

Then open: **http://localhost:3000**

---

**Backend**: http://localhost:8000  
**Frontend**: http://localhost:3000  
**API Docs**: http://localhost:8000/docs  

**Status**: ✅ COMPLETE & READY TO RUN
