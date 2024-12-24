"""
This file is use to define all route and controller under items
ex. {prefix}/items or {prefix}/items/*
"""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.dependencies.items import init_item
from app.application.dependencies.pagination import PaginationQuery
from app.application.exceptions import DefaultHTTPExceptionContent
from app.application.response import ItemsPaginationContent
from app.database.models.items import Item, ItemInput, ItemsORM

item_routes = APIRouter(prefix="/items")


@item_routes.post("/")
async def create_item(item_payload: ItemInput) -> Item:  # type: ignore[valid-type]
    """
    function use to create item record
    """
    item = await ItemsORM.create(
        **item_payload.model_dump()  # type: ignore[attr-defined]
    )
    return item


@item_routes.get("/", responses={404: {"model": DefaultHTTPExceptionContent}})
async def get_items(
    paginatioon_query: Annotated[PaginationQuery, Depends(PaginationQuery)]
) -> ItemsPaginationContent:  # type: ignore[valid-type]
    """
    function to get item records with pagination
    """
    items_queryset = ItemsORM.all()
    pagination = paginatioon_query.build_pagination(total=await items_queryset.count())
    items = (
        await items_queryset.order_by(paginatioon_query.sort + "id")
        .offset(paginatioon_query.offset)
        .limit(paginatioon_query.size)
    )
    return ItemsPaginationContent(data=items, pagination=pagination)


@item_routes.get("/{item_id}", responses={404: {"model": DefaultHTTPExceptionContent}})
async def get_item(item: Annotated[ItemsORM, Depends(init_item)]) -> Item:  # type: ignore[valid-type]
    """
    function to get item using id
    """
    return item


@item_routes.put("/{item_id}", responses={404: {"model": DefaultHTTPExceptionContent}})
async def update_item(
    item_payload: ItemInput, item: Annotated[ItemsORM, Depends(init_item)]  # type: ignore[valid-type]
) -> Item:  # type: ignore[valid-type]
    """
    function to update item using id and update payload
    """
    item = item.update_from_dict(
        item_payload.model_dump()  # type: ignore[attr-defined]
    )
    await item.save()
    return item


@item_routes.delete(
    "/{item_id}", responses={404: {"model": DefaultHTTPExceptionContent}}
)
async def delete_item(
    item: Annotated[ItemsORM, Depends(init_item)]
) -> Item:  # type: ignore[valid-type]
    """
    function delete item record using id
    """
    await item.delete()
    return item
