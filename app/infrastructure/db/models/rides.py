from app.infrastructure.db.db_settings import BaseTable
from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)


class Ride(BaseTable):
    ride_id: Mapped[int] = mapped_column(primary_key=True)
    driver_id: Mapped[int] = mapped_column(ForeignKey('drivers.driver_id'), nullable=False)
    car_id: Mapped[int] = mapped_column(ForeignKey('cars.car_id'), nullable=False)
    rating: Mapped[float] = mapped_column(default=5.0)

