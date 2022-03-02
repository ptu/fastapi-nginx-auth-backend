import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import Response

from app.startup import create_app, on_startup_event, on_shutdown_event

from app.conf import settings

from app.auth.api import router as auth_router

app: FastAPI = create_app(
    title=settings.TITLE, description=settings.DESCRIPTION, debug=settings.DEBUG
)


@app.on_event("startup")
async def startup() -> None:
    await on_startup_event(app)


@app.on_event("shutdown")
async def shutdown() -> None:
    await on_shutdown_event()


@app.get("/health", name="healthz", include_in_schema=False)
async def healthz() -> Response:
    return Response()


if settings.EXPOSE_METRICS:
    from starlette_exporter import handle_metrics

    @app.get("/metrics", name="metrics", include_in_schema=False)
    async def metrics(request: Request) -> Response:
        return handle_metrics(request)


app.include_router(auth_router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":  # pragma: no cover
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
