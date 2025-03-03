from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class Admin(Document):
    fullname: str
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Admin Sample",
                "email": "admin@email.com",
                "password": "3xt3m#",
            }
        }

    class Settings:
        name = "admin"


class AdminSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": {"username": "admin@email.com", "password": "3xt3m#"}
        }


class AdminData(BaseModel):
    fullname: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Admin Sample",
                "email": "admin@email.com",
            }
        }
