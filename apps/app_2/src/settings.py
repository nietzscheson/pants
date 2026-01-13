from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    hello: str = "Pants <3 Python Uv"
