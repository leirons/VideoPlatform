from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = "sqlite:///./app.core.db"

settings = Settings()


# LOG SETTINGS
LOG_FILE = 'logfile.log'
format = "{time} {level} {message}"
level = "DEBUG"
rotation = '100 KB'
compression = None

