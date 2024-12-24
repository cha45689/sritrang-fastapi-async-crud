"""
This file is use to store unit test code for item data model
"""

import pytest
from pydantic import ValidationError

from app.database.models.items import ItemInput
from tests.mock_data.item import (
    ItemInputFactory,
    invalid_item_input,
    missing_item_input,
)


def test_valid_item():
    """
    Test valid item data
    """
    ItemInputFactory.build()


@pytest.mark.parametrize("item_input", invalid_item_input)
def test_invalid_item(item_input):
    """
    Test invalid item data
    """
    try:  # noqa: SIM105
        ItemInputFactory.build(**item_input)
        raise Exception(  # pylint: disable=broad-exception-raised
            "Not raise expect error"
        )
    except ValidationError:
        pass


@pytest.mark.parametrize("item_input", missing_item_input)
def test_require_field_item(item_input):
    """
    Test invalid item data
    """
    try:  # noqa: SIM105
        ItemInput(**item_input)
        raise Exception(  # pylint: disable=broad-exception-raised
            "Not raise expect error"
        )
    except ValidationError:
        pass
