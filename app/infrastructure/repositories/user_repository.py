from app.infrastructure.db.models.users import User

from sqlalchemy.future import select
from app.infrastructure.db.db_settings import async_session
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import (
    update,
    delete
)


class UserRepository:
    model = User

    @classmethod
    async def get_all(cls):
        async with async_session() as session:
            query = select(cls.model)
            result = await session.execute(query)

            return result.scalars().all()

    '''
    @classmethod
    async def get_by_id(cls, user_id: int):
        async with async_session() as session:
            query = select(cls.model).where(User.user_id == user_id)
            result = await session.execute(query)

            return result.scalar_one_or_none()
    '''

    @classmethod
    async def get_by_params(cls, **params):
        async with async_session() as session:
            query = select(cls.model).filter_by(**params)
            result = await session.execute(query)

            return result.scalars().all()

    '''@classmethod
    async def get_by_role(cls, role: str):
        async with async_session() as session:
            query = select(cls.model).where(User.role == role)
            result = await session.execute(query)

            return result.scalar_one_or_none()'''


    @classmethod
    async def add(cls, **values):
        async with async_session() as session:
            async with session.begin():
                new_item = cls.model(**values)
                session.add(new_item)

                try:
                    await session.commit()
                except SQLAlchemyError as error:
                    await session.rollback()
                    raise error

                return new_item


    @classmethod
    async def update(cls, filter_by, **values):
        async with async_session() as session:
            async with session.begin():
                query = (
                    update(cls.model)
                    .where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
                    .values(**values)
                    .execution_options(synchronize_session='fetch')
                )
                await session.execute(query)

                try:
                    subquery = select(cls.model).where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
                    result = await session.execute(subquery)

                    await session.commit()
                except SQLAlchemyError as error:
                    await session.rollback()
                    raise error

                return result.scalar_one_or_none()


    @classmethod
    async def delete(cls, **filter_by):
        async with async_session() as session:
            async with session.begin():
                query = delete(cls.model).filter_by(**filter_by)
                result = await session.execute(query)

                try:
                    await session.commit()
                except SQLAlchemyError as error:
                    await session.rollback()
                    raise error

                return result.rowcount