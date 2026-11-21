from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Define your environment variables with type hints
    database_url: str = ""
    api_key: str = ""
    debug: bool = False
    secret_key: str = "bc2944d8c16c68368ed2a60710b5379f7d74805911d235ffaa0d467465b94d41"
    algorithm: str = "HS256"
    access_expiry_time: int = 30

    # In Pydantic v2, use model_config instead of class Config
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
