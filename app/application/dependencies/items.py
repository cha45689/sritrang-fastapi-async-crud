"""
Use to host dependencies injector of items routes
"""

from typing import Annotated

from fastapi import Path
from fastapi.exceptions import HTTPException
from tortoise.exceptions import DoesNotExist

from app.database.models.items import ItemsORM


async def init_item(item_id: Annotated[int, Path(title="id of item")]) -> ItemsORM:
    """
    method use to inject ItemsORM base on id
    """
    try:
        return await ItemsORM.get(id=item_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Item not found") from exc
