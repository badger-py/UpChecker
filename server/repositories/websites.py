from repositories.base import BaseCRUDCategory
from models import WebSite


class WebSiteRepository(BaseCRUDCategory):
    def __init__(self) -> None:
        super().__init__(WebSite)
