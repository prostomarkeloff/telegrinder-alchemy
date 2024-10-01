from telegrinder import Telegrinder, Token, API, logger
from bot.settings import SETTINGS
from bot import setup_handlers

api = API(token=Token(SETTINGS.BOT_TOKEN))
tg = Telegrinder(api)
logger.set_level("DEBUG")
setup_handlers(tg)

tg.run_forever()
