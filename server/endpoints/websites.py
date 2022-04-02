from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependices import get_db
from schemas.websites import WebSiteInSchema, WebSiteOutSchema, WebSiteOutShortSchema, WebSiteUpdateSchema
from services.websites import create_website_service, delete_user_service, get_all_websites_service, get_website_service, update_website_service


websites_endpoint = APIRouter(tags=["Websites"])


@websites_endpoint.get("/", response_model=List[WebSiteOutShortSchema])
async def get_all_websites_enpoint(
    db: Session = Depends(get_db),
    limit: int = 15, offset: int = 0
) -> List[WebSiteOutShortSchema]:
    return await get_all_websites_service(db=db, limit=limit, offset=offset)


@websites_endpoint.get("/{website_id}", response_model=WebSiteOutSchema)
async def get_website_enpoint(
    website_id: int,
    db: Session = Depends(get_db)
) -> WebSiteOutSchema:
    return await get_website_service(db=db, website_id=website_id)


@websites_endpoint.post("/", response_model=WebSiteOutShortSchema, status_code=status.HTTP_201_CREATED)
async def create_website_endpoint(website: WebSiteInSchema, db: Session = Depends(get_db)) -> WebSiteOutShortSchema:
    return await create_website_service(db=db, website=website)


@websites_endpoint.put("/{website_id}", response_model=WebSiteOutShortSchema)
async def update_website_endpoint(website_id: int, website: WebSiteUpdateSchema, db: Session = Depends(get_db)) -> WebSiteOutShortSchema:
    return await update_website_service(db=db, website_id=website_id, website=website)


@websites_endpoint.delete("/{website_id}")
async def delete_website_endpoint(website_id: int, db: Session = Depends(get_db)):
    await delete_user_service(db=db, website_id=website_id)
    return {"ok": True}
