from db import Base, SessionLocal, engine
from models import Category, Check, CheckType, MessageType, WebSite

fake = True

# create tables
Base.metadata.create_all(bind=engine)

with SessionLocal() as db:
    check_by_status_code = CheckType(
        name="Check by status code",
        description="If status code will equals to check_required_value in categoty, check will pased"
    )
    check_by_entry = CheckType(
        name="Check by etry some value in response",
        description="If check_required_value will in response body, check will pased"
    )

    message_type_telegram_bot = MessageType(
        name="Telegram Bot message",
        description="Message using Telgram Bot (you can set in settings)"
    )
    # TODO: e-mail
    db.add_all([check_by_status_code, check_by_entry,
               message_type_telegram_bot])
    db.commit()
    db.refresh(check_by_status_code)
    db.refresh(check_by_entry)
    db.refresh(message_type_telegram_bot)

print("db was creates sucesfully")

# NOTE: you can use Faker libary to create fake data

if fake:
    from random import random

    with SessionLocal() as db:
        google = WebSite(
            name="Google",
            url="https://www.google.com"
        )
        db.add(google)
        db.commit()
        db.refresh(google)
        main_page = Category(
            name="Main page of google.com",
            url="https://www.google.com/",
            website_id=google.id,
            check_type_id=check_by_status_code.id,
            check_required_value="200",
            message_type_id=message_type_telegram_bot.id,
            contact="12345789"
        )
        db.add(main_page)
        db.commit()
        db.refresh(main_page)
        checks = [Check(result=int(random() > 0.75),
                        category_id=main_page.id) for _ in range(100)]
        db.add_all(checks)
        db.commit()
