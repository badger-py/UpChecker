from os import getenv


SQLALCHEMY_DATABASE_URL = getenv(
    "SQLALCHEMY_DATABASE_URL", default="sqlite:///sql_app.db")
# SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

CONFIG_FILENAME = "settings.json"
