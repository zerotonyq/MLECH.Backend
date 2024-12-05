from app.domain.models.user import User

from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date, datetime


class UserQuery(User):
    user_id: int
    firstname: str
    lastname: str
    email: EmailStr = Field(..., description='Email address')

    class Config:
        orm_mode = True

