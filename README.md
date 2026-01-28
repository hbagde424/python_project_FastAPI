# Employee Management System - Full Stack

A complete, production-ready full-stack application for managing employees with FastAPI backend and React frontend.

## 📁 Project Structure

```
employee-management/
├── backend/                    # FastAPI Backend
│   ├── app/                   # Main application
│   ├── tests/                 # Unit tests
│   ├── run.py                 # Start backend
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # Environment config
│   ├── pytest.ini             # Pytest config
│   └── README.md              # Backend docs
│
├── frontend/                  # React Frontend
│   ├── src/                   # React source code
│   ├── index.html             # HTML template
│   ├── package.json           # NPM dependencies
│   ├── vite.config.js         # Vite config
│   ├── tailwind.config.js     # Tailwind config
│   └── README.md              # Frontend docs
│
└── Documentation/
    ├── START_HERE.md          # Getting started
    ├── QUICK_REFERENCE.md     # Quick commands
    ├── RUN_FULL_STACK.md      # Setup guide
    ├── INTEGRATION_GUIDE.md   # Integration details
    └── More...
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm

### Terminal 1: Start Backend

```bash
cd backend
python run.py
```

Backend will be available at: **http://localhost:8000**

### Terminal 2: Start Frontend

```bash
cd frontend
npm install  # First time only
npm run dev
```

Frontend will be available at: **http://localhost:3000**

## 📍 Important URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000/api/v1 |
| API Documentation | http://localhost:8000/docs |
| Health Check | http://localhost:8000/health |

## 📚 Documentation

### Getting Started
- **[START_HERE.md](START_HERE.md)** - Quick start guide
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Commands and URLs

### Setup & Configuration
- **[RUN_FULL_STACK.md](RUN_FULL_STACK.md)** - Detailed setup instructions
- **[backend/README.md](backend/README.md)** - Backend documentation
- **[frontend/README.md](frontend/README.md)** - Frontend documentation

### Development
- **[INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)** - How frontend and backend work together
- **[backend/DEVELOPMENT.md](backend/DEVELOPMENT.md)** - Backend development guide
- **[backend/ARCHITECTURE.md](backend/ARCHITECTURE.md)** - System architecture

## ✨ Features

### Employee Management
- ✅ Create, read, update, delete employees
- ✅ Filter by department
- ✅ View active employees
- ✅ Pagination support

### Dashboard
- ✅ Employee statistics
- ✅ Department breakdown
- ✅ Salary information
- ✅ Active rate percentage

### Technical
- ✅ Form validation
- ✅ Error handling
- ✅ Success notifications
- ✅ Responsive design
- ✅ API documentation

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI 0.128.0
- **Server**: Uvicorn 0.37.0
- **Database**: SQLAlchemy 2.0.46 + SQLite
- **Validation**: Pydantic 2.12.2
- **Testing**: Pytest 7.4.3

### Frontend
- **Framework**: React 18.2.0
- **Build Tool**: Vite 5.0.8
- **Styling**: Tailwind CSS 3.3.6
- **HTTP Client**: Axios 1.6.2
- **Routing**: React Router 6.20.0

## 📊 API Endpoints

### Employees
```
POST   /api/v1/employees                    Create
GET    /api/v1/employees                    List (paginated)
GET    /api/v1/employees/{id}               Get by ID
PUT    /api/v1/employees/{id}               Update
DELETE /api/v1/employees/{id}               Delete
GET    /api/v1/employees/department/{dept}  Filter by department
GET    /api/v1/employees/active/list        Get active employees
```

### Statistics
```
GET    /api/v1/stats                        Get statistics
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest                    # Run all tests
pytest -v               # Verbose output
pytest --cov=app        # With coverage
```

### Frontend Tests
```bash
cd frontend
npm test                # Run tests
npm test -- --coverage  # With coverage
```

## 🚀 Deployment

### Build Frontend
```bash
cd frontend
npm run build
```

### Deploy Backend
```bash
cd backend
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## 📝 Project Statistics

- **Backend Files**: 31 Python files
- **Frontend Files**: 11+ React files
- **API Endpoints**: 10+
- **Test Cases**: 10+
- **Documentation**: 12+ files
- **Total Code**: 5,000+ lines

## 🎯 Next Steps

1. **Start the Application**
   ```bash
   # Terminal 1
   cd backend && python run.py
   
   # Terminal 2
   cd frontend && npm run dev
   ```

2. **Open in Browser**
   - Frontend: http://localhost:3000
   - API Docs: http://localhost:8000/docs

3. **Test Features**
   - Create employees
   - View dashboard
   - Test all functionality

4. **Read Documentation**
   - Start with [START_HERE.md](START_HERE.md)
   - Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for commands

## 📞 Support

For issues or questions:
1. Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
2. Check [RUN_FULL_STACK.md](RUN_FULL_STACK.md)
3. Review backend logs: `backend/logs/app.log`
4. Check browser console: Press F12

## 📄 License

MIT License

---

**Status**: ✅ Production Ready  
**Backend**: http://localhost:8000  
**Frontend**: http://localhost:3000  
**API Docs**: http://localhost:8000/docs
