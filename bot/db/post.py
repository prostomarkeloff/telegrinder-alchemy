from bot.db import ModelBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime


class Post(ModelBase):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    writer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    text: Mapped[str]
    date: Mapped[datetime] = mapped_column(DateTime())
