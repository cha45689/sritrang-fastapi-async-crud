"""
This file is use to define all route and controller under items
ex. {prefix}/items or {prefix}/items/*
"""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.dependencies.items import init_item
from app.database.models.items import Item, ItemInput, ItemsORM

item_routes = APIRouter(prefix="/items")


@item_routes.post("/")
async def create_item(item_payload: ItemInput) -> Item:  # type: ignore[valid-type]
    """
    function use to create item record
    """
    item: ItemsORM = await ItemsORM.create(
        **item_payload.model_dump()  # type: ignore[attr-defined]
    )
    return item


@item_routes.get("/{item_id}")
async def get_item(item: Annotated[ItemsORM, Depends(init_item)]) -> Item:  # type: ignore[valid-type]
    """
    function use to create item record
    """
    return item


@item_routes.put("/{item_id}")
async def update_item(
    item_payload: ItemInput, item: Annotated[ItemsORM, Depends(init_item)]  # type: ignore[valid-type]
) -> Item:  # type: ignore[valid-type]
    """
    function use to create item record
    """
    item = item.update_from_dict(
        item_payload.model_dump()  # type: ignore[attr-defined]
    )
    await item.save()
    return item
