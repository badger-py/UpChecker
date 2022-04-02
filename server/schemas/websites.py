from typing import Optional, List

from pydantic import BaseModel, HttpUrl

from schemas.categories import CategoryOutSchema


class IDMixIn(BaseModel):
    id: int


class BaseWebSiteSchema(BaseModel):
    name: str
    url: HttpUrl
    is_paused: bool = False


class WebSiteInSchema(BaseWebSiteSchema):
    pass


class WebSiteOutShortSchema(BaseWebSiteSchema, IDMixIn):
    class Config:
        orm_mode = True


class WebSiteOutSchema(WebSiteOutShortSchema):
    categories: List[CategoryOutSchema]


class WebSiteUpdateSchema(BaseModel):
    name: Optional[str]
    url: Optional[HttpUrl]
    is_paused: Optional[bool]
