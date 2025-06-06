from betterconf import betterconf, DotenvProvider

PATH_TO_DOTENV = ".bot-env"


@betterconf(provider=DotenvProvider(PATH_TO_DOTENV, auto_load=True))
class Settings:
    BOT_TOKEN: str
    DB_URL: str


SETTINGS = Settings()
