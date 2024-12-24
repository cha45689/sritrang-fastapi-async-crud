"""
This is for fixture of mock item data and other mock data for item
"""

import factory
import pytest

from app.database.models.items import Item, ItemInput


class ItemInputFactory(factory.Factory):
    """
    Factory for creating ItemInput Object
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Define base object to create in this case ItemInput
        """

        model = ItemInput

    name = factory.Faker("pystr", min_chars=0, max_chars=255)
    description = factory.Faker("pystr", min_chars=0, max_chars=65535)


class ItemFactory(ItemInputFactory):
    """
    Factory for creating Item Object
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Define base object to create in this case Item
        """

        model = Item

    id = factory.Faker("pyint")


@pytest.fixture()
def valid_item_input() -> ItemInput:  # type: ignore
    """
    function use as fixture to generate random item input
    """
    return ItemInputFactory.build()


invalid_item_input = [
    {"name": 1, "description": 2},
    {"name": 1.5, "description": 2.5},
    {"name": ["s"], "description": ["a"]},
    {"name": None, "description": None},
    {"name": {"a"}, "description": {"b"}},
    {"name": {"a": "b"}, "description": {"b": "c"}},
    {"name": " " * 256, "description": " " * 65536},
]

missing_item_input = [{"name": "John"}, {"description": "John"}]

invalid_item = [
    {"id": 1, "name": 1, "description": 2},
    {"id": 1.0, "name": 1.5, "description": 2.5},
    {"id": [1], "name": ["s"], "description": ["a"]},
    {"id": None, "name": None, "description": None},
    {"id": {"c"}, "name": {"a"}, "description": {"b"}},
    {"id": {"c": "d"}, "name": {"a": "b"}, "description": {"b": "c"}},
    {"id": 1, "name": " " * 256, "description": " " * 65536},
]
missing_item = [
    {"id": 1, "name": "John"},
    {"name": "John", "description": "John"},
    {"id": 1, "description": "John"},
]
