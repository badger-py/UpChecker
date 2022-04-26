from pydantic import BaseModel
from sqlalchemy.orm import Session

from exceptions import NotFound


class BaseCRUDCategory():
    """Base repotitory with all CRUD
    it __init__ use:
        super().__init__(<model>)
    """
    def __init__(self, model) -> None:
        self.model = model

    async def get_by_pk(self, db: Session, pk: int):
        return db.query(self.model).get(pk)

    async def get_all(self, db: Session, limit: int = 15, offset: int = 0) -> list:
        return db.query(self.model).limit(limit).offset(offset).all()

    async def create(self, db: Session, schema: BaseModel):
        created = self.model(**schema.dict())

        db.add(created)
        db.commit()
        db.refresh(created)

        return created

    async def update(self, db: Session, pk: int, schema: BaseModel):
        obj = await self.get_by_pk(db=db, pk=pk)
        if obj is None:
            raise NotFound

        for key, value in schema.dict(exclude_unset=True).items():
            setattr(obj, key, value)

        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj

    async def delete(self, db: Session, pk: int) -> None:
        obj = await self.get_by_pk(db=db, pk=pk)
        if obj is None:
            raise NotFound

        db.delete(obj)
        db.commit()
