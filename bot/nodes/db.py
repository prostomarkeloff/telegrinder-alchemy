from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from telegrinder.node import scalar_node, global_node
from typing import AsyncGenerator
from bot.settings import SETTINGS


# it's global; called once
@scalar_node()
@global_node
class _SessionMaker(async_sessionmaker[AsyncSession]):
    @classmethod
    async def compose(cls) -> AsyncGenerator[async_sessionmaker[AsyncSession], None]:
        engine = create_async_engine(url=SETTINGS.DB_URL)
        maker = async_sessionmaker(engine)
        yield maker
        await engine.dispose()

@scalar_node()
class DBSession(AsyncSession):
    @classmethod
    async def compose(cls, maker: _SessionMaker) -> AsyncGenerator[AsyncSession, None]:
        session = maker()
        yield session
        await session.close()
