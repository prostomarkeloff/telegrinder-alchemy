from bot.nodes.db import DBSession
from telegrinder.node import ScalarNode, UserSource
from bot.db.user import User
from sqlalchemy import select


class DBUser(ScalarNode, User):  # type: ignore
    @classmethod
    async def compose(cls, user_src: UserSource, session: DBSession) -> User:
        result = (
            await session.execute(select(User).where(User.tg_id == user_src.id))
        ).scalar()
        if result:
            return result

        user = User(tg_id=user_src.id)
        session.add(user)
        await session.commit()

        return user
