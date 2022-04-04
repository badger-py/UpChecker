from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependices import get_db
from schemas.categories import CategoryInSchema, CategoryOutSchema, CategoryUpdateSchema
from services.categories import create_category_service, delete_category_service, get_all_categories_service, get_category_service, update_category_service


categories_endpoint = APIRouter(tags=["Categories"])


@categories_endpoint.get("/", response_model=List[CategoryOutSchema])
async def get_all_categories_enpoint(
    website_id: int, db: Session = Depends(get_db),
    limit: int = 15, offset: int = 0
) -> List[CategoryOutSchema]:
    return await get_all_categories_service(db=db, website_id=website_id, limit=limit, offset=offset)


@categories_endpoint.get("/{category_id}", response_model=CategoryOutSchema)
async def get_category_enpoint(
    category_id: int,
    db: Session = Depends(get_db)
) -> CategoryOutSchema:
    return await get_category_service(db=db, category_id=category_id)


@categories_endpoint.post("/", response_model=CategoryOutSchema, status_code=status.HTTP_201_CREATED)
async def create_category_endpoint(category: CategoryInSchema, db: Session = Depends(get_db)) -> CategoryOutSchema:
    return await create_category_service(db=db, category=category)


@categories_endpoint.put("/{category_id}", response_model=CategoryOutSchema)
async def update_category_endpoint(category_id: int, category: CategoryUpdateSchema, db: Session = Depends(get_db)) -> CategoryOutSchema:
    return await update_category_service(db=db, category_id=category_id, category=category)


@categories_endpoint.delete("/{category_id}")
async def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    await delete_category_service(db=db, category_id=category_id)
    return {"ok": True}
