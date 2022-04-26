from sqlalchemy.orm import Session

from models import Category
from repositories.base import BaseCRUDCategory


class CategoriesRepository(BaseCRUDCategory):
    def __init__(self) -> None:
        super().__init__(Category)

    async def get_all_by_website_id(
        self,
        db: Session, website_id: int,
        limit: int = 15, offset: int = 0
    ) -> list:
        return db.query(Category).filter_by(website_id=website_id).limit(limit).offset(offset).all()
