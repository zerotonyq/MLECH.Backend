from app.repositories.car_repository import CarRepository


async def get_all_cars():
    cars = await CarRepository.get_all()

    return cars


async def get_all_cars_with_predict():
    cars = await CarRepository.get_all_with_predict()

    return cars


async def get_car_by_id(car_id: int):
    car = await CarRepository.get_by_filter(car_id=car_id)

    return car


async def get_car_by_id_with_predict(car_id: int):
    car = await CarRepository.get_by_filter(car_id=car_id)

    return car


async def get_car_predicted_data(car_id: int):
    car_predicted_data = await CarRepository.get_by_filter(car_id=car_id)

    return car_predicted_data


async def get_car_rides(car_id: int):
    car_rides = await CarRepository.get_car_rides(car_id=car_id)

    return car_rides



async def get_car_fixes(car_id: int):
    car_fixes = await CarRepository.get_car_fixes(car_id=car_id)

    return car_fixes
