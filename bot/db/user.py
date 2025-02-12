from bot.db import ModelBase
from bot.db.post import Post
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(ModelBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int]
    posts: Mapped[list["Post"]] = relationship()
