from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase as _DBase


class ModelBase(_DBase, AsyncAttrs):
    pass


from bot.db.models.user import User

# through this we make it visible for the alembic
__all__ = ("ModelBase", "User")
