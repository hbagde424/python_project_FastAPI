# Quick Reference Guide

## 🚀 Start Application (30 seconds)

### Terminal 1: Backend
```bash
python run.py
```
→ http://localhost:8000

### Terminal 2: Frontend
```bash
cd frontend && npm run dev
```
→ http://localhost:3000

---

## 📍 Important URLs

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend | http://localhost:3000 | React App |
| Backend API | http://localhost:8000/api/v1 | API Endpoints |
| Swagger UI | http://localhost:8000/docs | API Documentation |
| ReDoc | http://localhost:8000/redoc | Alternative API Docs |
| Health Check | http://localhost:8000/health | Backend Status |

---

## 📁 Key Files

### Backend
- `run.py` - Start backend
- `app/main.py` - FastAPI app
- `app/api/v1/endpoints/employees.py` - Employee endpoints
- `app/services/employee_service.py` - Business logic
- `requirements.txt` - Dependencies

### Frontend
- `frontend/src/App.jsx` - Main component
- `frontend/src/pages/EmployeesPage.jsx` - Employees page
- `frontend/src/pages/DashboardPage.jsx` - Dashboard page
- `frontend/src/api/employees.js` - API calls
- `frontend/package.json` - Dependencies

---

## 🔧 Common Commands

### Backend

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python run.py

# Run tests
pytest

# Run tests with coverage
pytest --cov=app

# View logs
tail -f logs/app.log
```

### Frontend

```bash
# Install dependencies
npm install

# Start development
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linting
npm run lint
```

---

## 📊 API Endpoints

### Employees

```
POST   /employees              Create
GET    /employees              List (paginated)
GET    /employees/{id}         Get by ID
PUT    /employees/{id}         Update
DELETE /employees/{id}         Delete
GET    /employees/department/{dept}  Filter by department
GET    /employees/active/list  Get active
```

### Statistics

```
GET    /stats                  Get statistics
```

---

## 🎨 Frontend Pages

| Page | URL | Features |
|------|-----|----------|
| Employees | / | CRUD operations, pagination |
| Dashboard | /dashboard | Statistics, department breakdown |

---

## 📝 Create Employee Example

```bash
curl -X POST "http://localhost:8000/api/v1/employees" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "position": "Senior Developer",
    "department": "Engineering",
    "salary": 100000.0
  }'
```

---

## 🐛 Troubleshooting

### Backend Won't Start

```bash
# Check Python version
python --version  # Should be 3.8+

# Check virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Frontend Won't Start

```bash
# Clear cache
rm -rf node_modules package-lock.json

# Reinstall
npm install

# Start
npm run dev
```

### Port Already in Use

```bash
# Backend (port 8000)
lsof -i :8000  # Find process
kill -9 <PID>  # Kill process

# Frontend (port 3000)
lsof -i :3000  # Find process
kill -9 <PID>  # Kill process
```

### API Connection Error

1. Ensure backend is running: `python run.py`
2. Check API URL: `frontend/src/api/client.js`
3. Check CORS: `app/main.py`
4. Check browser console for errors

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| README.md | Backend documentation |
| frontend/README.md | Frontend documentation |
| ARCHITECTURE.md | System architecture |
| DEVELOPMENT.md | Development guide |
| FRONTEND_SETUP.md | Frontend setup |
| INTEGRATION_GUIDE.md | Integration details |
| RUN_FULL_STACK.md | Full stack guide |
| QUICK_REFERENCE.md | This file |

---

## 🔐 Environment Variables

### Backend (.env)

```
DATABASE_URL=sqlite:///./employees.db
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### Frontend

API URL in `src/api/client.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000/api/v1'
```

---

## 📦 Dependencies

### Backend

```
fastapi==0.128.0
uvicorn==0.37.0
sqlalchemy==2.0.46
pydantic==2.12.2
python-dotenv==1.1.0
email-validator==2.3.0
pytest==7.4.3
```

### Frontend

```
react@18.2.0
vite@5.0.8
tailwindcss@3.3.6
axios@1.6.2
react-router-dom@6.20.0
react-icons@4.12.0
react-toastify@9.1.3
```

---

## 🧪 Testing

### Backend

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_employees.py::test_create_employee

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=app
```

### Frontend

```bash
# Run tests
npm test

# Run with coverage
npm test -- --coverage
```

---

## 🚀 Deployment

### Build Frontend

```bash
cd frontend
npm run build
```

Output: `frontend/dist/`

### Deploy Backend

```bash
# Using Gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

### Docker

```bash
# Build backend
docker build -t employee-api .
docker run -p 8000:8000 employee-api

# Build frontend
docker build -t employee-frontend frontend/
docker run -p 3000:3000 employee-frontend
```

---

## 💡 Tips & Tricks

### Backend

1. **Hot Reload**: Set `DEBUG=True` in `.env`
2. **Database Reset**: Delete `employees.db` and restart
3. **API Testing**: Use Swagger UI at `/docs`
4. **Logging**: Check `logs/app.log`

### Frontend

1. **Hot Reload**: Automatic with Vite
2. **DevTools**: Press F12 to open
3. **React DevTools**: Install browser extension
4. **Network Tab**: Check API calls

---

## 🔗 Integration Points

### Frontend → Backend

```javascript
// API call example
const response = await employeeAPI.getAll(skip, limit)

// Error handling
try {
  await employeeAPI.create(data)
} catch (error) {
  toast.error(error.response?.data?.detail)
}
```

### Backend → Database

```python
# CRUD operation example
employee = employee_crud.create(db, employee_data)

# Query example
employees = db.query(Employee).filter(...).all()
```

---

## 📊 Database

### SQLite

```bash
# Connect to database
sqlite3 employees.db

# List tables
.tables

# View schema
.schema employees

# Query data
SELECT * FROM employees;

# Exit
.quit
```

---

## 🎯 Workflow

### Development

1. Start backend: `python run.py`
2. Start frontend: `npm run dev`
3. Make changes
4. Test in browser
5. Check console for errors
6. Commit changes

### Testing

1. Run backend tests: `pytest`
2. Run frontend tests: `npm test`
3. Manual testing in browser
4. Check API with Swagger UI

### Deployment

1. Build frontend: `npm run build`
2. Deploy backend to server
3. Deploy frontend to CDN
4. Update API URL if needed
5. Test in production

---

## 📞 Support

### Check These First

1. **Backend Issues**: Check `logs/app.log`
2. **Frontend Issues**: Check browser console (F12)
3. **API Issues**: Test with Swagger UI
4. **Connection Issues**: Verify both services running

### Documentation

- Backend: `README.md`
- Frontend: `frontend/README.md`
- Integration: `INTEGRATION_GUIDE.md`
- Full Stack: `RUN_FULL_STACK.md`

---

## ✅ Checklist

### Before Deployment

- [ ] Backend tests pass: `pytest`
- [ ] Frontend builds: `npm run build`
- [ ] No console errors
- [ ] API endpoints working
- [ ] Database backed up
- [ ] Environment variables set
- [ ] CORS configured
- [ ] Error handling tested

### After Deployment

- [ ] Frontend accessible
- [ ] Backend accessible
- [ ] API endpoints working
- [ ] Database connected
- [ ] Logging working
- [ ] Monitoring set up
- [ ] Backups configured

---

## 🎉 You're All Set!

**Backend**: http://localhost:8000  
**Frontend**: http://localhost:3000  
**API Docs**: http://localhost:8000/docs  

Happy coding! 🚀
