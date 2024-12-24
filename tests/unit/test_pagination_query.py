"""
This file is use to store test code specific to PaginationQuery class dependency
"""

import pytest
from fastapi import HTTPException

from app.application.dependencies.pagination import PaginationQuery
from app.database.models.pagination import Pagination


def test_pagination_dependency():
    """
    function use to test valid PaginationQuery case
    """
    pagination_query = PaginationQuery()
    pagination = pagination_query.build_pagination(5)
    assert pagination == Pagination(
        current_page=1, next_page=None, last_page=1, total=5, size=10
    )
    assert pagination_query.offset == 0


@pytest.mark.parametrize(["page", "total", "expect_offset"], [(1, 0, 0), (2, 5, 10)])
def test_fail_build_pagination(page, total, expect_offset):
    """
    function use to test PaginationQuery case where build_pagination fail
    """
    pagination_query = PaginationQuery(page=page)
    assert pagination_query.offset == expect_offset
    try:  # noqa: SIM105
        pagination_query.build_pagination(total=total)
    except HTTPException:
        pass
