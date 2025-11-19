from pydantic import BaseModel


class SingupRequest(BaseModel):
    name: str
    email: str
    password: str
