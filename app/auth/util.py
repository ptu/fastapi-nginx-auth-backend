from datetime import datetime, timedelta
from http.client import UNAUTHORIZED
from app.conf.settings import (
    COOKIE_NAME,
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from jose import JWTError, jwt
from typing import Optional
from fastapi import Request
from fastapi.exceptions import HTTPException


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def check_token(request: Request):
    if COOKIE_NAME in request.cookies:
        try:
            payload = jwt.decode(request.cookies[COOKIE_NAME], SECRET_KEY, ALGORITHM)
        except JWTError:
            raise HTTPException(status_code=UNAUTHORIZED)
        return payload
    raise HTTPException(status_code=UNAUTHORIZED)
