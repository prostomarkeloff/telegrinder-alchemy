from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILENAME = ".bot-env"


# TODO: rewrite to `betterconf` when 4.0 is out
class __Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILENAME, env_file_encoding="utf-8")

    BOT_TOKEN: str
    DB_URL: str


SETTINGS = __Settings()  # type: ignore # pyright doesn't care about pydantic
