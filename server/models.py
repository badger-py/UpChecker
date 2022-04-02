from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from db import Base


class WebSite(Base):
    __tablename__ = "websites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)
    is_paused = Column(Boolean, default=False)
    categories = relationship(
        "Category", back_populates="website", lazy="dynamic")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    url = Column(String(200), nullable=False)
    website_id = Column(Integer, ForeignKey("websites.id"))
    website = relationship("WebSite", back_populates="categories", lazy=True)
    check_type_id = Column(Integer, ForeignKey("check_types.id"))
    check_type = relationship("CheckType", lazy=True, uselist=False)
    # can be "200" if status code or value in response
    check_required_value = Column(String, nullable=False)

    message_type_id = Column(
        Integer, ForeignKey("message_types.id"))
    contact = Column(String)  # can be a chey id in Telegram or e-mail
    message_type = relationship("MessageType", lazy=True)
    checks = relationship("Check", back_populates="category", lazy="dynamic")


class BaseType():
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)


class CheckType(BaseType, Base):
    __tablename__ = "check_types"


class MessageType(BaseType, Base):
    __tablename__ = "message_types"


class Check(Base):
    __tablename__ = "checks"

    id = Column(Integer, primary_key=True, index=True)
    result = Column(Boolean, default=False)
    processed_at = Column(DateTime, default=datetime.utcnow)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="checks", lazy=True)
