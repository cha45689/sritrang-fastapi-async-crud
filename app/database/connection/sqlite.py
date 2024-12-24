"""
use for create function to register sqlite database
"""

from functools import partial

from tortoise.contrib.fastapi import RegisterTortoise

from app.application.config import settings

register_sqlite = partial(
    RegisterTortoise,
    db_url=settings.DB_URL,
    modules={"models": ["app.database.models.items"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
