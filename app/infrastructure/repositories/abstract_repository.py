from sqlalchemy.future import select
from app.infrastructure.db.db_settings import async_session
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import (
    update,
    delete
)


# TODO, all repositories has same code. Make AbstractRepository

