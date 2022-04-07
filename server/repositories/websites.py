from typing import List

from sqlalchemy.orm import Session

from models import WebSite
from schemas.websites import WebSiteInSchema, WebSiteUpdateSchema
from exceptions import NotFound


async def get_all_websites(
    db: Session,
    limit: int = 15, offset: int = 0
) -> List[WebSite]:
    return db.query(WebSite).limit(limit).offset(offset).all()


async def get_website(db: Session, website_id: int) -> WebSite:
    return db.query(WebSite).get(website_id)


async def create_website(db: Session, website: WebSiteInSchema) -> WebSite:
    created_website = WebSite(**website.dict())

    db.add(created_website)
    db.commit()
    db.refresh(created_website)

    return created_website


async def update_website(db: Session, website_id: int, website: WebSiteUpdateSchema) -> WebSite:
    edited_website = await get_website(db=db, website_id=website_id)
    if edited_website is None:
        raise NotFound

    for key, value in website.dict(exclude_unset=True).items():
        edited_website.__setattr__(key, value)

    db.add(edited_website)
    db.commit()
    db.refresh(edited_website)

    return edited_website


async def delete_website(db: Session, website_id: int):
    website = await get_website(db=db, website_id=website_id)
    if website is None:
        raise NotFound

    db.delete(website)
    db.commit()
