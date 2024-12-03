import os

from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr, StrictStr

load_dotenv()


class SiteSettings(BaseSettings):
    api_key: SecretStr = os.getenv("TG_API_KEY", None)
    host_api_two: StrictStr = os.getenv("JOKE_API", None)
    host_api_three: StrictStr = os.getenv("SINGLE_JOKE_API", None)
