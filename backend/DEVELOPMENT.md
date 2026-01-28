# Development Guide

## Setting Up Development Environment

### Prerequisites
- Python 3.8+
- pip or conda
- Git

### Initial Setup

```bash
# Clone repository
git clone <repository-url>
cd employee-management

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

## Project Structure Overview

```
app/
├── api/              # API routes and endpoints
├── core/             # Configuration and constants
├── crud/             # Database operations
├── db/               # Database setup
├── middleware/       # Request/response middleware
├── models/           # SQLAlchemy models
├── schemas/          # Pydantic schemas
├── services/         # Business logic
└── utils/            # Utilities and helpers
```

## Adding a New Feature

### Example: Add a Bonus Field to Employee

#### 1. Update Model (`app/models/employee.py`)
```python
class Employee(Base):
    __tablename__ = "employees"
    
    # ... existing fields ...
    bonus = Column(Float, default=0.0)  # Add this
```

#### 2. Update Schema (`app/schemas/employee.py`)
```python
class EmployeeBase(BaseModel):
    # ... existing fields ...
    bonus: float = Field(default=0.0, ge=0)

class EmployeeUpdate(BaseModel):
    # ... existing fields ...
    bonus: Optional[float] = Field(None, ge=0)
```

#### 3. Update Service (`app/services/employee_service.py`)
```python
# Add validation if needed
if employee_data.bonus < 0:
    raise InvalidInput("Bonus cannot be negative")
```

#### 4. Add Tests (`tests/test_employees.py`)
```python
def test_employee_with_bonus(client):
    response = client.post(
        "/api/v1/employees",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "position": "Developer",
            "department": "Engineering",
            "salary": 100000.0,
            "bonus": 10000.0
        }
    )
    assert response.status_code == 201
    assert response.json()["bonus"] == 10000.0
```

#### 5. Run Tests
```bash
pytest tests/test_employees.py::test_employee_with_bonus -v
```

## Common Development Tasks

### Running the Application

```bash
# Development mode (with auto-reload)
python run.py

# Production mode
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_employees.py

# Run specific test
pytest tests/test_employees.py::test_create_employee

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=app

# Run with coverage report
pytest --cov=app --cov-report=html
```

### Database Operations

```bash
# Reset database (delete and recreate)
rm employees.db
python run.py

# Access database directly
sqlite3 employees.db
```

### Code Quality

```bash
# Install linting tools
pip install flake8 black isort

# Format code
black app/ tests/

# Sort imports
isort app/ tests/

# Check code style
flake8 app/ tests/
```

## API Development Workflow

### 1. Define Schema
Create request/response models in `app/schemas/`

### 2. Create Model
Define database model in `app/models/`

### 3. Implement CRUD
Add database operations in `app/crud/`

### 4. Add Service Logic
Implement business logic in `app/services/`

### 5. Create Endpoint
Add API endpoint in `app/api/v1/endpoints/`

### 6. Write Tests
Add tests in `tests/`

### 7. Document
Add docstrings and update README

## Debugging

### Enable Debug Mode

Update `.env`:
```
DEBUG=True
```

### View Logs

```bash
# Real-time logs
tail -f logs/app.log

# Windows
Get-Content logs/app.log -Wait
```

### Use Python Debugger

```python
# In your code
import pdb; pdb.set_trace()

# Or use breakpoint() in Python 3.7+
breakpoint()
```

### FastAPI Debug Mode

```python
# In app/main.py
app = FastAPI(debug=True)
```

## Database Management

### Using SQLite

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

### Switching to PostgreSQL

1. Install PostgreSQL
2. Create database:
   ```bash
   createdb employee_db
   ```

3. Update `.env`:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/employee_db
   ```

4. Install psycopg2:
   ```bash
   pip install psycopg2-binary
   ```

5. Run application:
   ```bash
   python run.py
   ```

## Performance Optimization

### Database Indexing

```python
# In models
class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    department = Column(String, index=True)
```

### Query Optimization

```python
# Use pagination
employees = db.query(Employee).offset(skip).limit(limit).all()

# Use select specific columns
employees = db.query(Employee.id, Employee.name).all()

# Use eager loading
from sqlalchemy.orm import joinedload
employees = db.query(Employee).options(joinedload(Employee.department)).all()
```

### Caching

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_departments(db: Session):
    return db.query(Employee.department).distinct().all()
```

## Security Best Practices

### Input Validation

```python
# Use Pydantic for validation
class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    salary: float = Field(..., gt=0)
```

### SQL Injection Prevention

```python
# Use SQLAlchemy ORM (safe)
employee = db.query(Employee).filter(Employee.email == email).first()

# Never use string concatenation
# WRONG: db.query(f"SELECT * FROM employees WHERE email = '{email}'")
```

### CORS Configuration

```python
# In app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific domains
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

### Environment Variables

```python
# Use environment variables for secrets
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL  # From .env
```

## Deployment

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
```

Build and run:
```bash
docker build -t employee-api .
docker run -p 8000:8000 employee-api
```

### Environment Variables for Production

```
DATABASE_URL=postgresql://user:password@prod-db:5432/employee_db
DEBUG=False
HOST=0.0.0.0
PORT=8000
```

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

### Database Locked

```bash
# Delete database and restart
rm employees.db
python run.py
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
```

### Module Not Found

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

## Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push to remote
git push origin feature/new-feature

# Create pull request
# (on GitHub/GitLab)

# After review, merge to main
git checkout main
git merge feature/new-feature
```

## Code Style Guide

### Naming Conventions

```python
# Classes: PascalCase
class EmployeeService:
    pass

# Functions/methods: snake_case
def get_employee(employee_id: int):
    pass

# Constants: UPPER_SNAKE_CASE
MAX_EMPLOYEES = 1000

# Private: _leading_underscore
def _internal_helper():
    pass
```

### Docstrings

```python
def create_employee(db: Session, employee_data: EmployeeCreate) -> Employee:
    """
    Create a new employee.
    
    Args:
        db: Database session
        employee_data: Employee creation data
        
    Returns:
        Created employee object
        
    Raises:
        EmailAlreadyExists: If email already registered
    """
    pass
```

### Type Hints

```python
from typing import Optional, List

def get_employees(
    db: Session,
    skip: int = 0,
    limit: int = 10
) -> List[Employee]:
    pass

def get_employee_by_email(
    db: Session,
    email: str
) -> Optional[Employee]:
    pass
```

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Best Practices](https://pep8.org/)

## Getting Help

1. Check existing issues
2. Review documentation
3. Check logs in `logs/app.log`
4. Run tests to identify issues
5. Use debugger for complex issues
