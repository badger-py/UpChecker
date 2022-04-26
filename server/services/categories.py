from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.categories import CategoryInSchema, CategoryOutSchema, CategoryUpdateSchema
from repositories.categories import CategoriesRepository
from exceptions import NotFound

repository = CategoriesRepository()


async def get_all_categories_service(
    db: Session, website_id: int,
    limit: int = 15, offset: int = 0
) -> List[CategoryOutSchema]:
    categories = await repository.get_all_by_website_id(db=db, website_id=website_id, limit=limit, offset=offset)
    return [CategoryOutSchema.from_orm(i) for i in categories]


async def get_category_service(db: Session, category_id: int) -> CategoryOutSchema:
    category = await repository.get_by_pk(db=db, pk=category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Website not found")

    return CategoryOutSchema.from_orm(category)


async def create_category_service(db: Session, category: CategoryInSchema) -> CategoryOutSchema:
    return CategoryOutSchema.from_orm(await repository.create(db=db, schema=category))


async def update_category_service(db: Session, category_id: int, category: CategoryUpdateSchema) -> CategoryOutSchema:
    try:
        return CategoryOutSchema.from_orm(await repository.update(db=db, pk=category_id, schema=category))
    except NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given category not found"
        )


async def delete_category_service(db: Session, category_id: int):
    try:
        await repository.delete(db=db, pk=category_id)
    except NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given category not found"
        )
