from betterconf import betterconf


@betterconf
class Settings:
    BOT_TOKEN: str
    DB_URL: str


SETTINGS = Settings()
