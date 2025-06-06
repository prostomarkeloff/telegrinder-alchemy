from bot.nodes.db import UOW
from telegrinder.node import scalar_node, UserSource
from bot.db.models.user import User


@scalar_node
class DBUser:
    @classmethod
    async def compose(cls, user_src: UserSource, uow: UOW) -> User:
        user_id = user_src.id

        if user := await uow.users.get_by_id(user_id):
            return user

        async with uow:
            user = User(tg_id=user_id)
            await uow.users.create(user)

        return user
