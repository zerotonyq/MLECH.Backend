from app.repositories.ride_repository import RideRepository


async def get_all_rides():
    rides = await RideRepository.get_all()

    return rides


async def get_ride_by_id(ride_id: int):
    ride = await RideRepository.get_by_filter(ride_id=ride_id)

    return ride

