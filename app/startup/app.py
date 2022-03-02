import typing
from fastapi import FastAPI


def create_app(**app_kwargs: typing.Any) -> FastAPI:
    return FastAPI(**app_kwargs)
