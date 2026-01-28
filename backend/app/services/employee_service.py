from sqlalchemy.orm import Session
from app.crud import employee_crud
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.utils.exceptions import EmployeeNotFound, EmailAlreadyExists, DepartmentNotFound
from app.utils.logger import get_logger

logger = get_logger(__name__)

class EmployeeService:
    @staticmethod
    def create_employee(db: Session, employee_data: EmployeeCreate):
        """Create a new employee with validation"""
        logger.info(f"Creating employee with email: {employee_data.email}")
        
        existing = employee_crud.get_by_email(db, email=employee_data.email)
        if existing:
            logger.warning(f"Email already exists: {employee_data.email}")
            raise EmailAlreadyExists()
        
        employee = employee_crud.create(db=db, obj_in=employee_data)
        logger.info(f"Employee created successfully with ID: {employee.id}")
        return employee

    @staticmethod
    def get_employee(db: Session, employee_id: int):
        """Get employee by ID"""
        logger.info(f"Fetching employee with ID: {employee_id}")
        employee = employee_crud.get(db, id=employee_id)
        
        if not employee:
            logger.warning(f"Employee not found with ID: {employee_id}")
            raise EmployeeNotFound()
        
        return employee

    @staticmethod
    def get_all_employees(db: Session, skip: int = 0, limit: int = 10):
        """Get all employees with pagination"""
        logger.info(f"Fetching employees with skip={skip}, limit={limit}")
        employees = employee_crud.get_all(db, skip=skip, limit=limit)
        total = employee_crud.count(db)
        
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "items": employees
        }

    @staticmethod
    def update_employee(db: Session, employee_id: int, employee_update: EmployeeUpdate):
        """Update employee with validation"""
        logger.info(f"Updating employee with ID: {employee_id}")
        
        employee = employee_crud.get(db, id=employee_id)
        if not employee:
            logger.warning(f"Employee not found with ID: {employee_id}")
            raise EmployeeNotFound()
        
        # Check if new email is already in use
        if employee_update.email and employee_update.email != employee.email:
            existing = employee_crud.get_by_email(db, email=employee_update.email)
            if existing:
                logger.warning(f"Email already in use: {employee_update.email}")
                raise EmailAlreadyExists()
        
        updated_employee = employee_crud.update(db=db, db_obj=employee, obj_in=employee_update)
        logger.info(f"Employee updated successfully with ID: {employee_id}")
        return updated_employee

    @staticmethod
    def delete_employee(db: Session, employee_id: int):
        """Delete employee"""
        logger.info(f"Deleting employee with ID: {employee_id}")
        
        employee = employee_crud.get(db, id=employee_id)
        if not employee:
            logger.warning(f"Employee not found with ID: {employee_id}")
            raise EmployeeNotFound()
        
        employee_crud.delete(db=db, id=employee_id)
        logger.info(f"Employee deleted successfully with ID: {employee_id}")

    @staticmethod
    def get_employees_by_department(db: Session, department: str, skip: int = 0, limit: int = 10):
        """Get employees by department"""
        logger.info(f"Fetching employees from department: {department}")
        
        employees = employee_crud.get_by_department(db, department=department, skip=skip, limit=limit)
        total = employee_crud.count_by_department(db, department=department)
        
        if not employees:
            logger.warning(f"No employees found in department: {department}")
            raise DepartmentNotFound()
        
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "items": employees
        }

    @staticmethod
    def get_active_employees(db: Session, skip: int = 0, limit: int = 10):
        """Get active employees"""
        logger.info(f"Fetching active employees with skip={skip}, limit={limit}")
        employees = employee_crud.get_active_employees(db, skip=skip, limit=limit)
        total = employee_crud.count(db)
        
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "items": employees
        }
