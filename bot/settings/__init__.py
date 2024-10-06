from betterconf import betterconf
from dotenv import load_dotenv

ENV_FILENAME = ".bot-env"


@betterconf
class __Settings:
    BOT_TOKEN: str
    DB_URL: str

load_dotenv(ENV_FILENAME)
SETTINGS = __Settings()
