import os

from dotenv import find_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
    OUTPUT_DIR = os.path.join(BASE_DIR, "output")

    class Config:
        env_file = find_dotenv(".env.local")


settings = Settings()