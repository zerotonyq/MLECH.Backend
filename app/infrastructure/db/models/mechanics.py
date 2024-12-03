from app.infrastructure.db.db_settings import BaseTable
from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from datetime import date


class Mechanic(BaseTable):
    mechanic_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            'users.user_id',
            ondelete="CASCADE"
        ),
        nullable=False
    )
    birth_date: Mapped[date]
    sex: Mapped[bool]
    # TODO mechanic_rating: Mapped[float] Calculate dynamic and don't save at table? OR remove this
    car_times_repaired: Mapped[int] = mapped_column(nullable=False, default=0)

