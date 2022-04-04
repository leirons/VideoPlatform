from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')

settings = Settings()


# LOG SETTINGS
LOG_FILE = 'logfile.log'
format = "{time} {level} {message}"
level = "DEBUG"
rotation = '100 KB'
compression = None

