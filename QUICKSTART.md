# Quick Start Guide

## 1. Setup

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Run the Application

```bash
python run.py
```

Server starts at `http://localhost:8000`

## 3. Access API Documentation

Open in browser:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 4. Test the API

### Create an Employee

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

### List Employees

```bash
curl "http://localhost:8000/api/v1/employees"
```

### Get Single Employee

```bash
curl "http://localhost:8000/api/v1/employees/1"
```

### Update Employee

```bash
curl -X PUT "http://localhost:8000/api/v1/employees/1" \
  -H "Content-Type: application/json" \
  -d '{
    "salary": 120000.0
  }'
```

### Delete Employee

```bash
curl -X DELETE "http://localhost:8000/api/v1/employees/1"
```

### Get Statistics

```bash
curl "http://localhost:8000/api/v1/stats"
```

### Health Check

```bash
curl "http://localhost:8000/health"
```

## 5. Run Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_employees.py

# Run with coverage
pytest --cov=app
```

## 6. Project Structure Overview

```
app/
├── api/v1/endpoints/      # API routes
├── core/                  # Configuration
├── crud/                  # Database operations
├── db/                    # Database setup
├── middleware/            # Request logging
├── models/                # Database models
├── schemas/               # Request/response validation
├── services/              # Business logic
└── utils/                 # Helpers & exceptions
```

## 7. Key Files

- `run.py` - Application entry point
- `app/main.py` - FastAPI app setup
- `app/core/config.py` - Configuration
- `app/api/v1/endpoints/employees.py` - Employee endpoints
- `app/services/employee_service.py` - Business logic
- `tests/test_employees.py` - Unit tests

## 8. Common Tasks

### Add a New Endpoint

1. Create schema in `app/schemas/`
2. Create model in `app/models/`
3. Create CRUD in `app/crud/`
4. Create service in `app/services/`
5. Create endpoint in `app/api/v1/endpoints/`

### Change Database

Update `DATABASE_URL` in `.env`:
```
# PostgreSQL
DATABASE_URL=postgresql://user:password@localhost/dbname

# MySQL
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
```

### Enable Debug Mode

Update `.env`:
```
DEBUG=True
```

## 9. Troubleshooting

### Port Already in Use

Change port in `.env`:
```
PORT=8001
```

### Database Locked

Delete `employees.db` and restart:
```bash
rm employees.db
python run.py
```

### Import Errors

Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

## 10. Next Steps

- Read [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture
- Read [README.md](README.md) for full documentation
- Check `tests/test_employees.py` for API usage examples
- Explore Swagger UI at http://localhost:8000/docs
