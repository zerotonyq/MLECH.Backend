import re

from pydantic import BaseModel, EmailStr, Field, field_validator


class User(BaseModel):
    user_id: int
    firstname: str
    lastname: str
    email: EmailStr = Field(..., description='Email address')
    password_hash: str
    role: str


    @classmethod
    @field_validator('firstname')
    def validate_firstname(cls, firstname: str):
        if not firstname.isalpha():
            raise ValueError('Firstname should only contain letters')

        return firstname


    @classmethod
    @field_validator('lastname')
    def validate_lastname(cls, lastname: str):
        if not lastname.isalpha():
            raise ValueError('Lastname should only contain letters')

        return lastname


    @classmethod
    @field_validator('email')
    def validate_email(cls, email: str):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

        if email and not valid:
            raise ValueError('Email address is not valid')

        return email


    @classmethod
    @field_validator('role')
    def validate_role(cls, role: str):
        valid_roles = ['admin', 'driver', 'mechanic']

        if role not in valid_roles:
            raise ValueError(f'Role should be one of {valid_roles}')

        return role

