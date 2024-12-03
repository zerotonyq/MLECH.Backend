from app.infrastructure.db.db_settings import BaseTable
from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from datetime import datetime


class FixInfo(BaseTable):
    fix_info_id: Mapped[int] = mapped_column(primary_key=True)
    car_id: Mapped[int] = mapped_column(ForeignKey('cars.car_id'), nullable=False)
    mechanic_id: Mapped[int] = mapped_column(ForeignKey('mechanics.mechanic_id'), nullable=False)
    fix_datetime: Mapped[datetime] = mapped_column(default=datetime.now()) # TODO or only date ?
    work_type: Mapped[str] = mapped_column(nullable=False)
    destroy_degree: Mapped[float] = mapped_column(nullable=False)
    wor_duration: Mapped[int] = mapped_column(nullable=False)

