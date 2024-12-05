from fastapi import APIRouter

from app.infrastructure.dto.users.user_query import UserQuery
from app.routes.users.create import create_user


router = APIRouter(prefix='/users', tags=['Работа с пользователями'])


router.add_api_route("/", create_user, methods=["POST"], summary="Создание пользователя", response_model=UserQuery)