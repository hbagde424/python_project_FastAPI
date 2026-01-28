# Employee Management System

A production-grade FastAPI application for managing employees with enterprise architecture patterns.

## Features

- ✅ Complete CRUD operations for employees
- ✅ Department-based filtering
- ✅ Employee statistics and analytics
- ✅ Comprehensive error handling
- ✅ Request/response logging
- ✅ Pagination support
- ✅ Input validation
- ✅ Unit tests
- ✅ API documentation (Swagger UI)
- ✅ Health check endpoint

## Tech Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Database**: SQLAlchemy + SQLite (PostgreSQL ready)
- **Validation**: Pydantic
- **Testing**: Pytest
- **Logging**: Python logging

## Project Structure

```
app/
├── api/v1/endpoints/          # API endpoints
├── core/                      # Configuration & constants
├── crud/                      # Database operations
├── db/                        # Database setup
├── middleware/                # Request/response middleware
├── models/                    # SQLAlchemy models
├── schemas/                   # Pydantic schemas
├── services/                  # Business logic
├── utils/                     # Utilities & exceptions
└── main.py                    # FastAPI app
tests/                         # Unit tests
```

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python run.py
```

The API will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### Employees

#### Create Employee
```bash
POST /api/v1/employees
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "position": "Senior Developer",
  "department": "Engineering",
  "salary": 100000.0
}
```

#### List Employees
```bash
GET /api/v1/employees?skip=0&limit=10
```

#### Get Employee
```bash
GET /api/v1/employees/{id}
```

#### Update Employee
```bash
PUT /api/v1/employees/{id}
Content-Type: application/json

{
  "position": "Lead Developer",
  "salary": 120000.0
}
```

#### Delete Employee
```bash
DELETE /api/v1/employees/{id}
```

#### Get Employees by Department
```bash
GET /api/v1/employees/department/{department}
```

#### Get Active Employees
```bash
GET /api/v1/employees/active/list
```

### Statistics

#### Get Statistics
```bash
GET /api/v1/stats
```

Response:
```json
{
  "total_employees": 10,
  "active_employees": 9,
  "inactive_employees": 1,
  "average_salary": 95000.0,
  "total_salary": 950000.0,
  "departments": {
    "Engineering": {
      "count": 5,
      "avg_salary": 100000.0
    }
  }
}
```

### Health

#### Health Check
```bash
GET /health
```

## Testing

Run all tests:
```bash
pytest
```

Run with verbose output:
```bash
pytest -v
```

Run with coverage:
```bash
pytest --cov=app
```

Run specific test file:
```bash
pytest tests/test_employees.py
```

## Environment Variables

Create a `.env` file:
```
DATABASE_URL=sqlite:///./employees.db
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture documentation.

### Key Layers

1. **API Layer** - HTTP endpoints and routing
2. **Service Layer** - Business logic and validation
3. **CRUD Layer** - Database operations
4. **Database Layer** - SQLAlchemy ORM
5. **Models Layer** - Database schema
6. **Schemas Layer** - Request/response validation

## Logging

Logs are stored in `logs/app.log` with:
- Console output (INFO level)
- File output (DEBUG level)
- Request/response tracking
- Error logging

## Error Handling

The API returns meaningful error messages:

```json
{
  "detail": "Email already registered"
}
```

Common status codes:
- `200` - Success
- `201` - Created
- `204` - No Content
- `400` - Bad Request
- `404` - Not Found
- `422` - Validation Error
- `500` - Server Error

## Development

### Adding a New Endpoint

1. Create schema in `app/schemas/`
2. Create model in `app/models/`
3. Create CRUD in `app/crud/`
4. Create service in `app/services/`
5. Create endpoint in `app/api/v1/endpoints/`
6. Add tests in `tests/`

### Database Migrations

For production, use Alembic:
```bash
pip install alembic
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Performance Tips

1. Use pagination for large datasets
2. Add database indexes for frequently queried fields
3. Implement caching for statistics
4. Use connection pooling for production
5. Monitor slow queries

## Security Considerations

1. Add authentication (JWT, OAuth2)
2. Implement rate limiting
3. Add HTTPS in production
4. Validate all inputs
5. Use environment variables for secrets
6. Add CORS restrictions
7. Implement audit logging

## Deployment

### Docker

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

### Production Server

Use Gunicorn with Uvicorn workers:
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## Contributing

1. Create a feature branch
2. Make changes
3. Add tests
4. Run tests and linting
5. Submit pull request

## License

MIT License

## Support

For issues and questions, please create an issue in the repository.
