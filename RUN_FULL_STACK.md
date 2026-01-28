# Running Full Stack Application

Complete guide to run both backend and frontend together.

## Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn
- Git

## Quick Start (5 minutes)

### Terminal 1: Backend

```bash
# Navigate to project root
cd /path/to/employee-management

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run backend
python run.py
```

Backend will be available at: **http://localhost:8000**

### Terminal 2: Frontend

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run frontend
npm run dev
```

Frontend will be available at: **http://localhost:3000**

## Accessing the Application

### Frontend
- **URL**: http://localhost:3000
- **Employees Page**: http://localhost:3000/
- **Dashboard**: http://localhost:3000/dashboard

### Backend
- **API**: http://localhost:8000/api/v1
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## Detailed Setup

### Backend Setup

#### 1. Create Virtual Environment

```bash
python -m venv venv
```

#### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment

Create `.env` file (if not exists):
```
DATABASE_URL=sqlite:///./employees.db
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

#### 5. Run Backend

```bash
python run.py
```

You should see:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Frontend Setup

#### 1. Navigate to Frontend Directory

```bash
cd frontend
```

#### 2. Install Dependencies

```bash
npm install
```

This installs:
- React
- Vite
- Tailwind CSS
- Axios
- React Router
- React Icons
- React Toastify

#### 3. Run Development Server

```bash
npm run dev
```

You should see:
```
  VITE v5.0.8  ready in 234 ms

  ➜  Local:   http://localhost:3000/
  ➜  press h to show help
```

## Testing the Integration

### 1. Create an Employee

1. Open http://localhost:3000
2. Click "Add Employee"
3. Fill in the form:
   - Name: John Doe
   - Email: john@example.com
   - Position: Senior Developer
   - Department: Engineering
   - Salary: 100000
4. Click "Create"
5. You should see a success message

### 2. View Employees

1. The employee list should show the newly created employee
2. You can see all details in the table

### 3. Edit Employee

1. Click the edit icon (pencil) next to an employee
2. Modify the details
3. Click "Update"
4. Changes should be reflected immediately

### 4. Delete Employee

1. Click the delete icon (trash) next to an employee
2. Confirm deletion
3. Employee should be removed from the list

### 5. View Dashboard

1. Click "Dashboard" in the navigation
2. You should see:
   - Total employees count
   - Active/inactive employees
   - Average salary
   - Department breakdown
   - Total payroll

## Troubleshooting

### Backend Issues

#### Port 8000 Already in Use

```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows

# Or change port in .env
PORT=8001
```

#### Database Locked

```bash
# Delete database and restart
rm employees.db
python run.py
```

#### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### Backend Not Starting

1. Check Python version: `python --version` (should be 3.8+)
2. Check virtual environment is activated
3. Check all dependencies installed: `pip list`
4. Check logs for errors

### Frontend Issues

#### Port 3000 Already in Use

```bash
# Find process using port 3000
lsof -i :3000  # macOS/Linux
netstat -ano | findstr :3000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows

# Or change port in vite.config.js
server: {
  port: 3001,
}
```

#### API Connection Error

1. Ensure backend is running: `python run.py`
2. Check API URL in `frontend/src/api/client.js`
3. Check CORS configuration in backend
4. Check browser console for errors

#### Module Not Found

```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

#### Build Errors

```bash
# Clear Vite cache
rm -rf dist .vite
npm run build
```

## Development Workflow

### Making Changes

#### Backend Changes

1. Edit files in `app/` directory
2. Backend will auto-reload (if DEBUG=True)
3. Test changes in Swagger UI: http://localhost:8000/docs

#### Frontend Changes

1. Edit files in `frontend/src/` directory
2. Frontend will hot-reload automatically
3. Changes visible immediately in browser

### Running Tests

#### Backend Tests

```bash
pytest
pytest -v
pytest --cov=app
```

#### Frontend Tests

```bash
cd frontend
npm test
```

## Production Build

### Frontend Build

```bash
cd frontend
npm run build
```

This creates optimized build in `frontend/dist/`

### Backend Production

```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## Docker Setup (Optional)

### Backend Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run.py"]
```

Build and run:
```bash
docker build -t employee-api .
docker run -p 8000:8000 employee-api
```

### Frontend Docker

Create `frontend/Dockerfile`:
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "preview"]
```

Build and run:
```bash
docker build -t employee-frontend frontend/
docker run -p 3000:3000 employee-frontend
```

### Docker Compose

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=sqlite:///./employees.db
      - DEBUG=False

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

Run:
```bash
docker-compose up
```

## Monitoring

### Backend Logs

```bash
tail -f logs/app.log
```

### Frontend Console

Open browser DevTools (F12) and check Console tab

### API Testing

Use Swagger UI: http://localhost:8000/docs

## Performance Tips

### Backend

1. Use pagination for large datasets
2. Add database indexes
3. Implement caching
4. Monitor slow queries

### Frontend

1. Use React DevTools to identify re-renders
2. Implement code splitting
3. Optimize images
4. Monitor bundle size

## Security Checklist

- [ ] Change DEBUG to False in production
- [ ] Use HTTPS in production
- [ ] Add authentication
- [ ] Validate all inputs
- [ ] Use environment variables for secrets
- [ ] Implement rate limiting
- [ ] Add CORS restrictions
- [ ] Use strong database passwords

## Deployment Checklist

### Backend
- [ ] Set DEBUG=False
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up proper logging
- [ ] Configure CORS for production domain
- [ ] Use environment variables
- [ ] Set up database backups
- [ ] Monitor performance

### Frontend
- [ ] Update API URL to production
- [ ] Build optimized version
- [ ] Set up CDN
- [ ] Configure caching
- [ ] Set up monitoring
- [ ] Test all features

## Next Steps

1. **Customize Styling**
   - Edit `frontend/src/index.css`
   - Modify Tailwind config

2. **Add Features**
   - Add authentication
   - Add advanced filtering
   - Add export functionality
   - Add bulk operations

3. **Deploy**
   - Deploy backend to cloud
   - Deploy frontend to CDN
   - Set up CI/CD pipeline

4. **Monitor**
   - Set up error tracking
   - Set up performance monitoring
   - Set up uptime monitoring

## Resources

- [Backend Documentation](README.md)
- [Frontend Documentation](frontend/README.md)
- [Architecture Guide](ARCHITECTURE.md)
- [Integration Guide](INTEGRATION_GUIDE.md)
- [Development Guide](DEVELOPMENT.md)

## Support

For issues:
1. Check troubleshooting section
2. Review logs
3. Check browser console
4. Verify API connectivity
5. Check documentation

---

**Full Stack Application Ready!** 🚀

Backend: http://localhost:8000  
Frontend: http://localhost:3000
