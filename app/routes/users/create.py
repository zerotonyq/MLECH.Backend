from fastapi import Depends, HTTPException

from app.domain.models.user import User
from app.infrastructure.dto.users.user_query import UserQuery
from app.infrastructure.dto.users.create_command import UserCreateCommand
from app.infrastructure.repositories.user_repository import UserRepository


async def create_user(request_body: UserCreateCommand) -> UserQuery:
    try:
        user = await UserRepository.add(**request_body.model_dump())
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))