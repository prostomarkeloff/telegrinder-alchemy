from telegrinder import Dispatch, Message
from telegrinder.rules import Command, Argument
from bot.db.post import Post
from bot.nodes.user import DBUser
from bot.nodes.db import DBSession
from sqlalchemy import select
from datetime import datetime

posts_dp = Dispatch()


@posts_dp.message(
    Command(
        "create_post",
        Argument("contents", validators=[lambda cts: cts if len(cts) > 0 else None]),
    )
)
async def create_post(
    message: Message, contents: str, user: DBUser, session: DBSession
):
    new_post = Post(text=contents, writer_id=user.id, date=datetime.now())
    session.add(new_post)
    await session.commit()

    await message.answer(
        "Wow! You've successfully posted a new post!\nLook at it with `/get_posts`"
    )


@posts_dp.message(Command("get_posts"))
async def get_posts(message: Message, session: DBSession):
    posts = (await session.execute(select(Post))).scalars()
    answer = "Posts:\n\n"
    for post in posts:
        answer += f"{post.id}: {post.text}\nWritten by user with id {post.writer_id} at {post.date}"
        answer += "\n\n"

    await message.answer(answer)
