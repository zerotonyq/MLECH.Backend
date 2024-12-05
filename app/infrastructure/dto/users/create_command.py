from app.domain.models.user import User

from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date, datetime


class UserCreateCommand(User):
    firstname: str
    lastname: str
    email: EmailStr = Field(..., description='Email address')
    password_hash: str
    role: str

