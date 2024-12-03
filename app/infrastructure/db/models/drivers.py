from app.infrastructure.db.db_settings import BaseTable
from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from datetime import date


class Driver(BaseTable):
    driver_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            'users.user_id',
            ondelete="CASCADE"
        ),
        nullable=False
    )
    birt_date: Mapped[date]
    sex: Mapped[bool]
    # TODO driver_rating: Mapped[float] Calculate dynamic and don't save at table?
    driver_rides: Mapped[int] = mapped_column(nullable=False, default=0)
    driver_time_accidents: Mapped[int] = mapped_column(nullable=False, default=0)
    driver_license_number: Mapped[str] = mapped_column(unique=True, nullable=False)

