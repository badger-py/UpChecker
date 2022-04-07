from typing import List

from sqlalchemy.orm import Session

from models import Category
from schemas.categories import CategoryInSchema, CategoryUpdateSchema
from exceptions import NotFound


async def get_all_categories(
    db: Session, website_id: int,
    limit: int = 15, offset: int = 0
) -> List[Category]:
    return db.query(Category).filter_by(website_id=website_id).limit(limit).offset(offset).all()


async def get_category(db: Session, category_id: int) -> Category:
    return db.query(Category).get(category_id)


async def create_category(db: Session, category: CategoryInSchema) -> Category:
    created_category = Category(**category.dict())
    db.add(created_category)
    db.commit()
    db.refresh(created_category)

    return created_category


async def update_category(db: Session, category_id: int, category: CategoryUpdateSchema) -> Category:
    edited_category = await get_category(db=db, category_id=category_id)
    if edited_category is None:
        raise NotFound

    for key, value in category.dict(exclude_unset=True).items():
        edited_category.__setattr__(key, value)

    db.add(edited_category)
    db.commit()
    db.refresh(edited_category)

    return edited_category


async def delete_category(db: Session, category_id: int):
    category = await get_category(db=db, category_id=category_id)
    if category is None:
        raise NotFound

    db.delete(category)
    db.commit()
