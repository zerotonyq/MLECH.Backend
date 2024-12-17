from app.infrastructure.db.database import async_session
from app.infrastructure.db.models.cars import Car
from app.infrastructure.db.models.fix_info import FixInfo
from app.infrastructure.db.models.rides import Ride
from app.infrastructure.db.models.ride_info import RideInfo
from app.infrastructure.db.models.cars_predicted_data import CarPredictedData
from app.repositories.repository import Repository

from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError


class CarRepository(Repository):
    model = Car


    @classmethod
    async def get_by_id(cls, car_id: int):
        async with async_session() as session:
            query = select(cls.model).where(cls.model.car_id == car_id)
            result = await session.execute(query)

            return result.scalar_one_or_none()


    @classmethod
    async def get_car_rides(cls, car_id: int):
        async with async_session() as session:
            try:
                query = (
                    select(
                        cls.model.car_id,
                        Ride,
                        RideInfo
                    )
                    .join(Ride, Ride.car_id == Car.car_id)
                    .join(RideInfo, Ride.ride_id == RideInfo.ride_id)
                    .where(cls.model.car_id == car_id)
                )
                result = await session.execute(query)
                car_rides = [dict(row) for row in result.mappings()]

                return car_rides
            except SQLAlchemyError as error:
                raise error


    @classmethod
    async def get_car_fixes(cls, car_id: int):
        async with async_session() as session:
            try:
                query = (
                    select(
                        cls.model.car_id,
                        FixInfo
                    )
                    .join(FixInfo, FixInfo.car_id == car_id)
                    .where(cls.model.car_id == car_id)
                )
                result = await session.execute(query)
                car_fixes = [dict(row) for row in result.mappings()]

                return car_fixes
            except SQLAlchemyError as error:
                raise error


    @classmethod
    async def get_car_predicted_data(cls, car_id: int):
        async with async_session() as session:
            try:
                query = (
                    select(
                        cls.model.car_id,
                        CarPredictedData.target_reg,
                        CarPredictedData.target_class
                    )
                    .where(CarPredictedData.car_id == car_id)
                )
                result = await session.execute(query)
                car_predicted_data = [dict(row) for row in result.mappings()]

                return car_predicted_data
            except SQLAlchemyError as error:
                raise error

