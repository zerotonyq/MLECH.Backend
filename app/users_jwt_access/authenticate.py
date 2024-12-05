from pydantic import EmailStr

from app.infrastructure.repositories.user_repository import User, UserRepository
from app.users_jwt_access.pass_hashing import verify_password


async def authenticate(email: EmailStr, password: str):
    potential_users = await UserRepository.get_by_params(email=email)

    if len(potential_users) == 0:
        return None

    user = potential_users[0]

    if not verify_password(password, user.password):
        return None

    return user