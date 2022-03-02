from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware


def setup_prometheus_middleware(app: FastAPI) -> None:  # pragma: no cover
    # Attach Prometheus middleware to the app.
    app.add_middleware(PrometheusMiddleware, group_paths=True)


middlewares = [setup_prometheus_middleware]
