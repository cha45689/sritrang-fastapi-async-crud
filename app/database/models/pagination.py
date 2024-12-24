"""
This file is use to host pagination datamodel for response purpose
"""

from pydantic import BaseModel


class Pagination(BaseModel):
    """
    class use to define field in pagination
    """

    current_page: int
    next_page: int | None
    last_page: int
    total: int
    size: int
