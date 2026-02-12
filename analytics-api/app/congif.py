from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- SERVER SETTINGS ---
    server_host: str = Field(default="0.0.0.0", serialization_alias="SERVER_HOST")
    server_port: int = Field(default=8000, serialization_alias="SERVER_PORT")
    debug: bool = Field(default=True, serialization_alias="DEBUG")
    project_name: str = Field(default="app_api", serialization_alias="PROJECT_NAME")


settings = Settings()

