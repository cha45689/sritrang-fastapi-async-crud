"""
Use to host pagination api input through query param
"""

import math
from typing import Annotated

from fastapi import HTTPException, Query

from app.database.models.pagination import Pagination


class PaginationQuery:
    """
    Class use to control how pagination is b
    """

    def __init__(
        self,
        page: Annotated[int, Query(gt=0)] = 1,
        size: Annotated[int, Query(gt=0)] = 10,
        desc: Annotated[bool, Query()] = False,
    ):
        self.page = page
        self.size = size
        self.sort: str = "-" if desc else ""

    def build_pagination(self, total: int) -> Pagination:
        """
        Method use to build pagination base on query param input store in object and total record input
        """
        if total < 1:
            raise HTTPException(status_code=404, detail="There is no item found")
        if self.offset > total:
            raise HTTPException(status_code=404, detail="Current page exceed last page")
        last_page = math.ceil(total / self.size)
        return Pagination(
            current_page=self.page,
            next_page=self.page + 1 if self.page < last_page else None,
            last_page=last_page,
            total=total,
            size=self.size,
        )

    @property
    def offset(self) -> int:
        """
        property for offset for using in query and pagination calculation
        """
        return (self.page - 1) * self.size
