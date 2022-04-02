from typing import List
from pydantic import AnyHttpUrl, BaseModel


class IDMixIn(BaseModel):
    id: int


class BaseType(BaseModel):
    name: str
    description: str


class BaseTypeOutSchema(BaseType, IDMixIn):
    class Config:
        orm_mode = True


class BaseCategory(BaseModel):
    name: str
    url: AnyHttpUrl
    check_type: BaseTypeOutSchema
    check_required_value: str

    contact: str
    message_type: BaseTypeOutSchema
    # checks: List[BaseTypeOutSchema]


class CategoryOutSchema(BaseCategory, IDMixIn):
    class Config:
        orm_mode = True
