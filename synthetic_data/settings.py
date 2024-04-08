import os

from dotenv import find_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
    OUTPUT_DIR: str = os.path.join(BASE_DIR, "output")
    PROMPT_TEMPLATE_DIR: str = os.path.join(BASE_DIR, "templates")
    EXAMPLE_JSON_DIR: str = os.path.join(BASE_DIR, "examples")
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = find_dotenv(".env.local")


settings = Settings()