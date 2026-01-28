from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import EmployeeService
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse,
    EmployeeListResponse
)

router = APIRouter()

@router.post("", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    """Create a new employee"""
    return EmployeeService.create_employee(db, employee)

@router.get("", response_model=EmployeeListResponse)
def get_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get all employees with pagination"""
    return EmployeeService.get_all_employees(db, skip=skip, limit=limit)

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    """Get employee by ID"""
    return EmployeeService.get_employee(db, employee_id)

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee_update: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    """Update employee details"""
    return EmployeeService.update_employee(db, employee_id, employee_update)

@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    """Delete employee"""
    EmployeeService.delete_employee(db, employee_id)

@router.get("/department/{department}", response_model=EmployeeListResponse)
def get_employees_by_department(
    department: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get employees by department"""
    return EmployeeService.get_employees_by_department(db, department, skip=skip, limit=limit)

@router.get("/active/list", response_model=EmployeeListResponse)
def get_active_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get active employees"""
    return EmployeeService.get_active_employees(db, skip=skip, limit=limit)
