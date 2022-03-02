FROM python:3.8-slim

ARG USER=api

ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install --no-cache-dir --upgrade poetry

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/code" \
    "$USER"

WORKDIR /code

COPY ./poetry.lock ./pyproject.toml ./poetry.toml ./healthcheck.py /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-dev

COPY ./app /code/app

RUN chown -R ${USER} /code

USER ${USER}
EXPOSE 8000/tcp

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
   CMD [ "python", "/code/healthcheck.py" ]

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]