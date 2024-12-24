"""
This file is use to define all route and controller under items
ex. {prefix}/items or {prefix}/items/*
"""

from fastapi import APIRouter

from app.database.models.items import Item, ItemInput, ItemsORM

item_routes = APIRouter(prefix="/items")


@item_routes.post("/")
async def create_item(item_payload: ItemInput) -> Item:  # type: ignore[valid-type]
    """
    function use to create item record
    """
    item: ItemsORM = await ItemsORM.create(**item_payload.dict())  # type: ignore[attr-defined]
    return item
