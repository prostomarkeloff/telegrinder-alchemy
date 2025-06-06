from bot.db.base import ModelBase
from sqlalchemy.orm import mapped_column, Mapped


class User(ModelBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
