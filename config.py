# Reading env variables

from pathlib import Path
from pydantic_settings import BaseSettings

class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"

class Config(BaseConfig):
    GOOGLE_API_KEY: str | None = None
    HUGGINGFACEHUB_API_TOKEN: str | None = None

config: Config = Config()