from fastapi import (
    HTTPException,
    Path,
    Body,
    Depends
)

from app.infrastructure.schemas.car_schemas import SCarUpdate
from app.infrastructure.schemas.cars_predicted_data_schemas import SCarPredictedDataUpdate
from app.repositories.car_repository import CarRepository
from app.repositories.car_predicted_data_repository import CarPredictedDataRepository


async def update_car_by_id(car_id: int = Path(...), request_body: SCarUpdate = Body(...)):
    try:
        car_data = request_body.model_dump(exclude_none=True)

        car = await CarRepository.update(
            {"car_id": car_id},
            **car_data
        )

        if car is None:
            raise HTTPException(status_code=404, detail="Car not found")

        return car
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


async def update_car_predicted_data_by_id(car_id: int = Path(...), request_body: SCarPredictedDataUpdate = Body(...)):
    try:
        update_data = request_body.model_dump(exclude_none=True)

        car_predicted_data = await CarPredictedDataRepository.update(
            {"car_id": car_id},
            **update_data
        )

        if car_predicted_data is None:
            raise HTTPException(status_code=404, detail="Car Predicted Data not found")

        return car_predicted_data
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

