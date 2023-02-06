from pydantic import BaseModel, Field


class Domain(BaseModel):
    """Domain schema class"""
    id: str
    domain: str
    isActive: bool
    isPrivate: bool
    createdAt: str
    updatedAt: str


class Domains(BaseModel):
    """Domains schema class"""
    hydra_member: list[Domain] = Field(alias="hydra:member")
    hydra_totalItems: int = Field(alias="hydra:totalItems")
