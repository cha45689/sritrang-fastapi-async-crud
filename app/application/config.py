"""
This file is use to host all configuration for the application
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    This class is use to host all generic settings by prioritize reading from
    env variable then .env file
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DB_URL: str


settings = Settings()
