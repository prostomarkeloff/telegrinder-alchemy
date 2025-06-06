from telegrinder import Dispatch, Message
from telegrinder.rules import StartCommand

start_dp = Dispatch()


@start_dp.message(StartCommand())
async def start_command(message: Message):
    await message.answer("Hi there!")
