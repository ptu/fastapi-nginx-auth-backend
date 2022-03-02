from pydantic import BaseModel


class PasswordData(BaseModel):
    pw: str
