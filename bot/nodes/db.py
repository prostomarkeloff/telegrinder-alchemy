from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from telegrinder.node import ScalarNode, global_node
from typing import AsyncGenerator
from bot.settings import SETTINGS


# it's global; called once
@global_node
class _SessionMaker(ScalarNode, async_sessionmaker[AsyncSession]):
    @classmethod
    async def compose(cls) -> AsyncGenerator[async_sessionmaker[AsyncSession], None]:
        engine = create_async_engine(url=SETTINGS.DB_URL)
        maker = async_sessionmaker(engine)
        yield maker
        await engine.dispose()


class DBSession(ScalarNode, AsyncSession):
    @classmethod
    async def compose(cls, maker: _SessionMaker) -> AsyncGenerator[AsyncSession, None]:
        session = maker()
        yield session
        await session.close()
