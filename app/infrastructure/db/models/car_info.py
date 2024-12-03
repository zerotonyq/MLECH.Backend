from app.infrastructure.db.db_settings import BaseTable
from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from datetime import date


class CarInfo(BaseTable):
    car_id: Mapped[int] = mapped_column(
        ForeignKey(
            'cars.car_id',
            ondelete="CASCADE"
        ),
        primary_key=True
    )
    model: Mapped[str] = mapped_column(nullable=False)
    car_type: Mapped[str] = mapped_column(nullable=False) # sedan, coupe, etc.
    fuel_type: Mapped[str]
    year_to_start: Mapped[date] = mapped_column(nullable=False)
    year_to_work: Mapped[date] = mapped_column(nullable=False)

