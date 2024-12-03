from app.infrastructure.db.db_settings import BaseTable
from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from datetime import datetime


class RideInfo(BaseTable):
    ride_id: Mapped[int] = mapped_column(ForeignKey('rides.ride_id'), primary_key=True)
    ride_datetime: Mapped[datetime] = mapped_column(nullable=False)
    ride_duration: Mapped[int] = mapped_column(nullable=False)
    ride_cost: Mapped[int] = mapped_column(nullable=False)
    speed_avg: Mapped[float]
    speed_max: Mapped[float]
    stop_times: Mapped[int] = mapped_column(nullable=False, default=0)
    distance: Mapped[float] = mapped_column(nullable=False)
    refueling: Mapped[int] = mapped_column(nullable=False, default=0)
    user_ride_quality: Mapped[float] = mapped_column(nullable=False)
    deviation_normal: Mapped[float] = mapped_column(nullable=False)

