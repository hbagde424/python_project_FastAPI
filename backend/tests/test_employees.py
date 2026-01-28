import pytest
from fastapi.testclient import TestClient

def test_create_employee(client):
    """Test creating a new employee"""
    response = client.post(
        "/api/v1/employees",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "position": "Senior Developer",
            "department": "Engineering",
            "salary": 100000.0
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert data["id"] is not None

def test_create_duplicate_email(client):
    """Test creating employee with duplicate email"""
    employee_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "position": "Senior Developer",
        "department": "Engineering",
        "salary": 100000.0
    }
    
    # Create first employee
    client.post("/api/v1/employees", json=employee_data)
    
    # Try to create with same email
    response = client.post("/api/v1/employees", json=employee_data)
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]

def test_get_employees(client):
    """Test getting all employees"""
    # Create an employee first
    client.post(
        "/api/v1/employees",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "position": "Senior Developer",
            "department": "Engineering",
            "salary": 100000.0
        }
    )
    
    response = client.get("/api/v1/employees")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 1
    assert len(data["items"]) >= 1

def test_get_employee_by_id(client):
    """Test getting employee by ID"""
    # Create an employee
    create_response = client.post(
        "/api/v1/employees",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "position": "Senior Developer",
            "department": "Engineering",
            "salary": 100000.0
        }
    )
    employee_id = create_response.json()["id"]
    
    # Get the employee
    response = client.get(f"/api/v1/employees/{employee_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == employee_id
    assert data["name"] == "John Doe"

def test_get_nonexistent_employee(client):
    """Test getting non-existent employee"""
    response = client.get("/api/v1/employees/999")
    assert response.status_code == 404

def test_update_employee(client):
    """Test updating employee"""
    # Create an employee
    create_response = client.post(
        "/api/v1/employees",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "position": "Senior Developer",
            "department": "Engineering",
            "salary": 100000.0
        }
    )
    employee_id = create_response.json()["id"]
    
    # Update the employee
    response = client.put(
        f"/api/v1/employees/{employee_id}",
        json={
            "position": "Lead Developer",
            "salary": 120000.0
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["position"] == "Lead Developer"
    assert data["salary"] == 120000.0

def test_delete_employee(client):
    """Test deleting employee"""
    # Create an employee
    create_response = client.post(
        "/api/v1/employees",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "position": "Senior Developer",
            "department": "Engineering",
            "salary": 100000.0
        }
    )
    employee_id = create_response.json()["id"]
    
    # Delete the employee
    response = client.delete(f"/api/v1/employees/{employee_id}")
    assert response.status_code == 204
    
    # Verify it's deleted
    response = client.get(f"/api/v1/employees/{employee_id}")
    assert response.status_code == 404

def test_get_employees_by_department(client):
    """Test getting employees by department"""
    # Create employees in different departments
    client.post(
        "/api/v1/employees",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "position": "Senior Developer",
            "department": "Engineering",
            "salary": 100000.0
        }
    )
    
    client.post(
        "/api/v1/employees",
        json={
            "name": "Jane Smith",
            "email": "jane@example.com",
            "position": "Sales Manager",
            "department": "Sales",
            "salary": 80000.0
        }
    )
    
    # Get employees from Engineering
    response = client.get("/api/v1/employees/department/Engineering")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 1
    assert all(emp["department"] == "Engineering" for emp in data["items"])

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
