from telegrinder import Dispatch, Message
from telegrinder.rules import StartCommand, Command
from bot.nodes.user import DBUser

start_dp = Dispatch()


@start_dp.message(StartCommand())
async def start_command(message: Message):
    await message.answer(
        f"Hi there, {message.from_user.first_name}!\nDo you want to register? Go on /register command!"
    )


@start_dp.message(Command("register"))
async def register(message: Message, user: DBUser):
    await message.answer(
        f"WOW! You have successfully registered (via node!).\nYour id in DB is {user.id}"
    )
