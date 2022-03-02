from starlette.config import Config
from starlette.datastructures import Secret

# from starlette.datastructures import URL, Secret

config = Config(".env")

TITLE = "EXAMPLE API"
DESCRIPTION = "description of example API"

ENVIRONMENT = config("ENVIRONMENT", cast=str, default="development")
DEBUG = config("DEBUG", cast=bool, default=False)

EXPOSE_METRICS = config("EXPOSE_METRICS", cast=bool, default=False)


# openssl rand -hex 32
SECRET_KEY = config("SECRET_KEY", cast=str)
ALGORITHM = config("ALGORITHM", cast=str, default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30
)
COOKIE_NAME = config("COOKIE_NAME", cast=str, default="NoCookie")
LOGOUT_REDIRECT = config("LOGOUT_REDIRECT", cast=str, default="/")

PASSWORD = config("PASSWORD", cast=str)
