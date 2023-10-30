from pydantic import BaseModel, Field

from typing import Optional


class MessageFromTo(BaseModel):
    name: str
    address: str


class Message(BaseModel):
    id: str
    accountId: str
    msgid: str
    from_: MessageFromTo = Field(alias="from")
    to: list[MessageFromTo]
    subject: str
    intro: str
    seen: bool
    isDeleted: bool
    hasAttachments: bool
    size: int
    downloadUrl: str
    createdAt: str
    updatedAt: str


class MessageView(BaseModel):
    first: str = Field(alias="hydra:first")
    last: str = Field(alias="hydra:last")
    previous: str = Field(alias="hydra:previous")
    next: str = Field(alias="hydra:next")


class MessageSearch(BaseModel):
    template: str = Field(alias="hydra:template")
    variableRepresentation: str = Field(alias="hydra:variableRepresentation")
    mapping: dict = Field(alias="hydra:mapping")


class Attachment(BaseModel):
    id: str
    filename: str
    contentType: str
    disposition: str
    transferEncoding: str
    related: bool
    size: int
    downloadUrl: str


class OneMessage(BaseModel):
    id: str
    accountId: str
    msgid: str
    from_: MessageFromTo = Field(alias="from")
    to: list[MessageFromTo]
    cc: list[str]
    bcc: list[str]
    subject: str
    flagged: bool
    isDeleted: bool
    verifications: dict
    retention: bool
    retentionDate: str
    text: str
    html: list[str]
    hasAttachments: bool
    attachments: Optional[list[Attachment]] = None
    size: int
    downloadUrl: str
    createdAt: str
    updatedAt: str


class Mapping(BaseModel):
    type: str = Field(alias="@type")
    variable: str
    property: str
    required: bool


class Messages(BaseModel):
    hydra_member: list[Message] = Field(alias="hydra:member")
    hydra_totalItems: int = Field(alias="hydra:totalItems")
    hydra_view: MessageView = Field(None, alias="hydra:view")


class MessageSource(BaseModel):
    id: str
    downloadUrl: str
    data: str
