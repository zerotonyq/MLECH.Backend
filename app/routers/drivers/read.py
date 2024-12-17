from sqlalchemy.testing.suite.test_reflection import users

from app.repositories.driver_repository import DriverRepository


async def get_all_drivers():
    drivers = await DriverRepository.get_all()

    return drivers


async def get_driver_by_id(driver_id: int):
    driver = await DriverRepository.get_by_driver_id(driver_id=driver_id)

    return driver