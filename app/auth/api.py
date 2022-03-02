from http.client import NO_CONTENT, UNAUTHORIZED
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from starlette.responses import Response

from .schemas import PasswordData
from .util import create_access_token, check_token
from app.conf.settings import ACCESS_TOKEN_EXPIRE_MINUTES, PASSWORD, COOKIE_NAME, LOGOUT_REDIRECT

router = APIRouter()


@router.get("/")
async def check_auth(token: str = Depends(check_token)) -> Response:
    return Response(status_code=NO_CONTENT)


@router.post("/login")
async def check_pass(password: PasswordData) -> Response:
    if password.pw == PASSWORD:
        response = Response(status_code=NO_CONTENT)
        response.set_cookie(
            key=COOKIE_NAME,
            value=create_access_token({"overninethousand": 9001}),
            httponly=True,
            expires=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        )
        return response
    raise HTTPException(status_code=UNAUTHORIZED)


@router.get("/logout")
async def logout() -> Response:
    response = RedirectResponse(LOGOUT_REDIRECT)
    response.set_cookie(key=COOKIE_NAME, value="", httponly=True)
    return response
