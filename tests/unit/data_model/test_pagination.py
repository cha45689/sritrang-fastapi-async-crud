"""
this module is use to store test code to test validation rul eof Pagination model
"""

import pytest
from pydantic import ValidationError

from app.database.models.pagination import Pagination
from tests.mock_data.pagination import invalid_pagination, valid_pagination


@pytest.mark.parametrize("pagination", valid_pagination)
def test_valid_pagination(pagination):
    """
    Test valid case for Pagination model
    """
    Pagination(**pagination)


@pytest.mark.parametrize("pagination", invalid_pagination)
def test_invalid_pagination(pagination):
    """
    Test invalid case for Pagination model which should raise ValidationError
    """
    try:  # noqa: SIM105
        Pagination(**pagination)
        raise Exception(  # pylint: disable=broad-exception-raised
            "Not raise expect error"
        )
    except ValidationError:
        pass
