from app.infrastructure.db.db_settings import BaseTable
from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from datetime import datetime


class RefreshToken(BaseTable):
    token_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            'users.user_id',
            ondelete='CASCADE'
        ),
        nullable=False
    )
    refresh_token: Mapped[str] = mapped_column(nullable=False)
    expires_at: Mapped[datetime] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now())
    is_revoked: Mapped[bool] = mapped_column(default=False)