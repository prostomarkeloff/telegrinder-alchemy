from bot.db import ModelBase
from sqlalchemy.orm import Mapped, mapped_column


class User(ModelBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int]
