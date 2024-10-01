from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase as _DBase


class ModelBase(_DBase, AsyncAttrs):
    pass


from bot.db.user import User

__all__ = (
    "ModelBase",
    "User",
)
