from typing import Optional
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

    contact: str
    # FIXME: message type
    # checks: List[BaseTypeOutSchema]


class CategoryInSchema(BaseCategory):
    check_type_id: int
    check_required_value: str

    website_id: int
    message_type_id: int


class CategoryOutSchema(BaseCategory, IDMixIn):
    check_type: BaseTypeOutSchema
    check_required_value: str

    message_type: BaseTypeOutSchema

    class Config:
        orm_mode = True


class CategoryUpdateSchema(BaseModel):
    name: Optional[str]
    url: Optional[AnyHttpUrl]

    contact: Optional[str]
    message_type_id: Optional[int]
    check_type_id: Optional[int]
    check_required_value: Optional[str]
