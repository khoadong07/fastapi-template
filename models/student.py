from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel, EmailStr


class Student(Document):
    fullname: str
    email: EmailStr
    course_of_study: str
    year: int
    gpa: float

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Student Sample",
                "email": "student@email.com",
                "course_of_study": "Engineering",
                "year": 4,
                "gpa": "3.76",
            }
        }

    class Settings:
        name = "student"
