from telegrinder.bot.bot import Telegrinder


def setup_handlers(tg: Telegrinder):
    from bot.handlers.start import start_dp

    tg.dispatch.load(start_dp)
