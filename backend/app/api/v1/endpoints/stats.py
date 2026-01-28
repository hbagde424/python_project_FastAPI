from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import get_db
from app.models.employee import Employee
from pydantic import BaseModel

router = APIRouter()

class StatsResponse(BaseModel):
    total_employees: int
    active_employees: int
    inactive_employees: int
    average_salary: float
    total_salary: float
    departments: dict

@router.get("", response_model=StatsResponse)
def get_statistics(db: Session = Depends(get_db)):
    """Get employee statistics"""
    
    total = db.query(func.count(Employee.id)).scalar() or 0
    active = db.query(func.count(Employee.id)).filter(Employee.is_active == True).scalar() or 0
    inactive = total - active
    
    avg_salary = db.query(func.avg(Employee.salary)).scalar() or 0.0
    total_salary = db.query(func.sum(Employee.salary)).scalar() or 0.0
    
    # Department breakdown
    dept_stats = db.query(
        Employee.department,
        func.count(Employee.id).label("count"),
        func.avg(Employee.salary).label("avg_salary")
    ).group_by(Employee.department).all()
    
    departments = {
        dept: {"count": count, "avg_salary": float(avg_sal or 0)}
        for dept, count, avg_sal in dept_stats
    }
    
    return {
        "total_employees": total,
        "active_employees": active,
        "inactive_employees": inactive,
        "average_salary": float(avg_salary),
        "total_salary": float(total_salary),
        "departments": departments
    }
