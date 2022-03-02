import logging

from fastapi import FastAPI

from app.conf import settings, log_filter

# from .exception_handlers import exception_handlers
from .middlewares import middlewares

logger = logging.getLogger(__name__)


def _setup_middlewares(app: FastAPI) -> None:  # pragma: no cover
    for middleware in middlewares:
        middleware(app)


# def _setup_exception_handlers(app: FastAPI) -> None:  # pragma: no cover
#     for exc, handler in exception_handlers:
#         app.add_exception_handler(exc, handler)  # type: ignore


def _log_settings() -> None:  # pragma: no cover
    logger.info(
        "Middlewares and ExceptionHandlers loaded",
        extra={"eventName": "setting-loading"},
    )


async def on_startup_event(app: FastAPI) -> None:  # pragma: no cover
    _setup_middlewares(app)
    # _setup_exception_handlers(app)
    logging.getLogger("uvicorn.access").addFilter(log_filter.EndpointCheckFilter())
    _log_settings()


async def on_shutdown_event() -> None:  # pragma: no cover
    pass


__all__ = ("on_startup_event", "on_shutdown_event")
