from datetime import timedelta
from jose import jwt
from app.config import get_jwt_params
from datetime import datetime

from fastapi import (
    Request,
    HTTPException,
    status
)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(hours=2)

    to_encode.update({"exp": expire})

    jwt_params = get_jwt_params()

    encoded = jwt.encode(to_encode, jwt_params['secret_key'], algorithm=jwt_params['algorithm'])

    return encoded


def get_token(request: Request) -> str:
    token = request.cookies.get('user_access_token')

    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access token not found')

    return token


def refresh_access_token(request: Request) -> str:
    pass
    # TODO