from pydantic import BaseModel


class Account(BaseModel):
    id: str
    address: str
    quota: int
    used: int
    isDisabled: bool
    isDeleted: bool
    createdAt: str
    updatedAt: str


class Token(BaseModel):
    id: str
    token: str
