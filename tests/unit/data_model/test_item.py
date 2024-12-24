"""
This file is use to store unit test code for item data model
"""

import pytest
from pydantic import ValidationError

from app.database.models.items import Item, ItemInput
from tests.mock_data.item import (
    ItemFactory,
    ItemInputFactory,
    invalid_item,
    invalid_item_input,
    missing_item,
    missing_item_input,
)


def test_valid_item_input():
    """
    Test valid item data
    """
    ItemInputFactory.build()


@pytest.mark.parametrize("item_input", invalid_item_input)
def test_invalid_item_input(item_input):
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
def test_require_field_item_input(item_input):
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


def test_valid_item():
    """
    Test valid item data
    """
    ItemFactory.build()


@pytest.mark.parametrize("item", invalid_item)
def test_invalid_item(item):
    """
    Test invalid item data
    """
    try:  # noqa: SIM105
        ItemFactory.build(**item)
        raise Exception(  # pylint: disable=broad-exception-raised
            "Not raise expect error"
        )
    except ValidationError:
        pass


@pytest.mark.parametrize("item", missing_item)
def test_require_field_item(item):
    """
    Test invalid item data
    """
    try:  # noqa: SIM105
        Item(**item)
        raise Exception(  # pylint: disable=broad-exception-raised
            "Not raise expect error"
        )
    except ValidationError:
        pass
