# Frontend-Backend Integration Guide

## Overview

This guide explains how the React frontend integrates with the FastAPI backend.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    React Frontend                           │
│                  (http://localhost:3000)                    │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Pages (EmployeesPage, DashboardPage)               │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Components (Form, Table, Cards)                    │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Custom Hooks (useEmployees)                        │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  API Client (Axios)                                 │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                          ↓ HTTP
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                          │
│                  (http://localhost:8000)                    │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  API Routes (/api/v1/employees, /api/v1/stats)     │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Service Layer (Business Logic)                     │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  CRUD Layer (Database Operations)                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  SQLAlchemy ORM                                     │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ↓                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  SQLite Database                                    │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. Fetching Employees

```
User clicks "Employees" page
    ↓
EmployeesPage component mounts
    ↓
useEmployees hook called
    ↓
employeeAPI.getAll() called
    ↓
Axios sends GET /api/v1/employees
    ↓
Backend receives request
    ↓
EmployeeService.get_all_employees()
    ↓
CRUD layer queries database
    ↓
Database returns employees
    ↓
Response sent to frontend
    ↓
EmployeeTable component renders
```

### 2. Creating Employee

```
User fills form and clicks "Create"
    ↓
EmployeeForm.handleSubmit()
    ↓
Form validation
    ↓
employeeAPI.create(data)
    ↓
Axios sends POST /api/v1/employees
    ↓
Backend receives request
    ↓
EmployeeService.create_employee()
    ↓
Email uniqueness check
    ↓
CRUD layer creates record
    ↓
Database saves employee
    ↓
Response sent to frontend
    ↓
Toast notification shown
    ↓
Employee list refreshed
```

### 3. Updating Employee

```
User clicks edit button
    ↓
EmployeeForm populated with data
    ↓
User modifies fields
    ↓
User clicks "Update"
    ↓
employeeAPI.update(id, data)
    ↓
Axios sends PUT /api/v1/employees/{id}
    ↓
Backend receives request
    ↓
EmployeeService.update_employee()
    ↓
Email uniqueness check (if changed)
    ↓
CRUD layer updates record
    ↓
Database updates employee
    ↓
Response sent to frontend
    ↓
Toast notification shown
    ↓
Employee list refreshed
```

## API Endpoints

### Employees

#### List Employees
```
GET /api/v1/employees?skip=0&limit=10

Response:
{
  "total": 10,
  "skip": 0,
  "limit": 10,
  "items": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "position": "Senior Developer",
      "department": "Engineering",
      "salary": 100000.0,
      "is_active": true,
      "created_at": "2026-01-28T10:00:00",
      "updated_at": "2026-01-28T10:00:00"
    }
  ]
}
```

#### Create Employee
```
POST /api/v1/employees

Request:
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "position": "Product Manager",
  "department": "Product",
  "salary": 95000.0
}

Response:
{
  "id": 2,
  "name": "Jane Smith",
  "email": "jane@example.com",
  "position": "Product Manager",
  "department": "Product",
  "salary": 95000.0,
  "is_active": true,
  "created_at": "2026-01-28T10:05:00",
  "updated_at": "2026-01-28T10:05:00"
}
```

#### Get Employee
```
GET /api/v1/employees/1

Response:
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "position": "Senior Developer",
  "department": "Engineering",
  "salary": 100000.0,
  "is_active": true,
  "created_at": "2026-01-28T10:00:00",
  "updated_at": "2026-01-28T10:00:00"
}
```

#### Update Employee
```
PUT /api/v1/employees/1

Request:
{
  "salary": 110000.0,
  "position": "Lead Developer"
}

Response:
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "position": "Lead Developer",
  "department": "Engineering",
  "salary": 110000.0,
  "is_active": true,
  "created_at": "2026-01-28T10:00:00",
  "updated_at": "2026-01-28T10:05:00"
}
```

#### Delete Employee
```
DELETE /api/v1/employees/1

Response: 204 No Content
```

### Statistics

#### Get Statistics
```
GET /api/v1/stats

Response:
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
    },
    "Sales": {
      "count": 3,
      "avg_salary": 80000.0
    }
  }
}
```

## Error Handling

### Frontend Error Handling

```javascript
try {
  const response = await employeeAPI.create(data)
  // Success
  toast.success('Employee created successfully!')
} catch (error) {
  // Error handling
  const message = error.response?.data?.detail || 'Failed to create employee'
  toast.error(message)
}
```

### Backend Error Responses

#### 400 Bad Request
```json
{
  "detail": "Email already registered"
}
```

#### 404 Not Found
```json
{
  "detail": "Employee not found"
}
```

#### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "salary"],
      "msg": "ensure this value is greater than 0",
      "type": "value_error.number.not_gt"
    }
  ]
}
```

#### 500 Server Error
```json
{
  "detail": "Internal server error"
}
```

## CORS Configuration

The backend is configured to accept requests from:
- http://localhost:3000
- http://localhost:3001
- http://127.0.0.1:3000
- http://127.0.0.1:3001

To add more origins, edit `app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "https://yourdomain.com",  # Add production domain
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Request/Response Cycle

### Request Headers
```
GET /api/v1/employees HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Accept: application/json
Origin: http://localhost:3000
```

### Response Headers
```
HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Credentials: true
```

## Debugging

### Frontend Debugging

1. **Browser DevTools**
   - Open DevTools (F12)
   - Check Network tab for API calls
   - Check Console for errors

2. **React DevTools**
   - Install React DevTools extension
   - Inspect component state and props

3. **Axios Interceptors**
   - Log requests and responses in `src/api/client.js`

### Backend Debugging

1. **Check Logs**
   ```bash
   tail -f logs/app.log
   ```

2. **API Documentation**
   - Visit http://localhost:8000/docs
   - Test endpoints directly

3. **Database**
   ```bash
   sqlite3 employees.db
   SELECT * FROM employees;
   ```

## Performance Optimization

### Frontend

1. **Pagination**
   - Limit items per page (default: 10)
   - Implement lazy loading

2. **Caching**
   - Cache employee list
   - Implement cache invalidation

3. **Code Splitting**
   - Lazy load pages
   - Lazy load components

### Backend

1. **Database Indexing**
   - Indexes on email, department, is_active

2. **Query Optimization**
   - Use pagination
   - Select specific columns

3. **Caching**
   - Cache statistics
   - Cache department list

## Testing Integration

### Frontend Tests

```javascript
// Test API call
test('fetches employees', async () => {
  const response = await employeeAPI.getAll()
  expect(response.data.items).toBeDefined()
})
```

### Backend Tests

```python
# Test endpoint
def test_get_employees(client):
    response = client.get("/api/v1/employees")
    assert response.status_code == 200
    assert "items" in response.json()
```

## Deployment

### Frontend Deployment

1. Build the application
   ```bash
   npm run build
   ```

2. Deploy to hosting service
   - Vercel
   - Netlify
   - GitHub Pages
   - AWS S3 + CloudFront

### Backend Deployment

1. Deploy to server
   - Heroku
   - AWS EC2
   - Google Cloud
   - DigitalOcean

2. Update API URL in frontend
   ```javascript
   const API_BASE_URL = 'https://api.yourdomain.com/api/v1'
   ```

## Troubleshooting

### CORS Error

**Error**: `Access to XMLHttpRequest blocked by CORS policy`

**Solution**:
1. Check backend CORS configuration
2. Verify frontend URL is in allowed origins
3. Check browser console for exact error

### API Connection Error

**Error**: `Failed to fetch`

**Solution**:
1. Ensure backend is running
2. Check API URL in frontend
3. Check network connectivity
4. Check firewall settings

### Validation Error

**Error**: `Email already registered`

**Solution**:
1. Use unique email
2. Check database for existing email
3. Clear database if needed

### Timeout Error

**Error**: `Request timeout`

**Solution**:
1. Check backend performance
2. Increase timeout in axios
3. Optimize database queries

## Best Practices

1. **Error Handling**
   - Always handle errors gracefully
   - Show user-friendly messages

2. **Loading States**
   - Show loading indicators
   - Disable buttons during requests

3. **Validation**
   - Validate on frontend
   - Validate on backend

4. **Security**
   - Use HTTPS in production
   - Validate all inputs
   - Sanitize data

5. **Performance**
   - Use pagination
   - Implement caching
   - Optimize queries

## Resources

- [React Documentation](https://react.dev)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Axios Documentation](https://axios-http.com)
- [REST API Best Practices](https://restfulapi.net)

---

**Integration Complete!** 🎉
