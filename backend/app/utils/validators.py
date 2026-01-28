import re
from typing import Optional

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_salary(salary: float) -> bool:
    """Validate salary is positive"""
    return salary > 0

def validate_name(name: str) -> bool:
    """Validate name is not empty and reasonable length"""
    return 1 <= len(name.strip()) <= 100

def validate_department(department: str) -> bool:
    """Validate department name"""
    return 1 <= len(department.strip()) <= 100

def sanitize_string(value: str) -> str:
    """Remove leading/trailing whitespace"""
    return value.strip() if isinstance(value, str) else value
