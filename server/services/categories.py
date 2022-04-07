from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.categories import CategoryInSchema, CategoryOutSchema, CategoryUpdateSchema
from repositories.categories import create_category, delete_category, get_all_categories, get_category, update_category
from exceptions import NotFound


async def get_all_categories_service(
    db: Session, website_id: int,
    limit: int = 15, offset: int = 0
) -> List[CategoryOutSchema]:
    categories = await get_all_categories(db=db, website_id=website_id, limit=limit, offset=offset)
    return [CategoryOutSchema.from_orm(i) for i in categories]


async def get_category_service(db: Session, category_id: int) -> CategoryOutSchema:
    category = await get_category(db=db, category_id=category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Website not found")

    return CategoryOutSchema.from_orm(category)


async def create_category_service(db: Session, category: CategoryInSchema) -> CategoryOutSchema:
    return CategoryOutSchema.from_orm(await create_category(db=db, category=category))


async def update_category_service(db: Session, category_id: int, category: CategoryUpdateSchema) -> CategoryOutSchema:
    try:
        return CategoryOutSchema.from_orm(await update_category(db=db, category_id=category_id, category=category))
    except NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given category not found"
        )


async def delete_category_service(db: Session, category_id: int):
    try:
        await delete_category(db=db, category_id=category_id)
    except NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given category not found"
        )
