"""
This file is for Response of api except one that could be define directly using model or error relate
"""

from typing import Any, List

from pydantic import BaseModel

from app.database.models.items import Item
from app.database.models.pagination import Pagination


class PaginationContent(BaseModel):
    """
    class for general format pagination result content
    """

    data: List[Any]
    pagination: Pagination


class ItemsPaginationContent(PaginationContent):
    """
    class for documentation of item pagination result content
    """

    data: List[Item]  # type: ignore[valid-type]
