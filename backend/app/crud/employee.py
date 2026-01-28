from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from typing import Optional, List

class CRUDEmployee(CRUDBase[Employee, EmployeeCreate, EmployeeUpdate]):
    def get_by_email(self, db: Session, email: str) -> Optional[Employee]:
        return db.query(self.model).filter(self.model.email == email).first()

    def get_by_department(self, db: Session, department: str, skip: int = 0, limit: int = 10) -> List[Employee]:
        return db.query(self.model).filter(
            self.model.department == department
        ).offset(skip).limit(limit).all()

    def get_active_employees(self, db: Session, skip: int = 0, limit: int = 10) -> List[Employee]:
        return db.query(self.model).filter(
            self.model.is_active == True
        ).offset(skip).limit(limit).all()

    def count_by_department(self, db: Session, department: str) -> int:
        return db.query(self.model).filter(self.model.department == department).count()

employee_crud = CRUDEmployee(Employee)
