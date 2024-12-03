from app.infrastructure.db.db_settings import BaseTable

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)


class Car(BaseTable):
    car_id: Mapped[int] = mapped_column(primary_key=True)
    car_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    is_rented: Mapped[bool] = mapped_column(nullable=False, default=False)

