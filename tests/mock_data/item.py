"""
This is for fixture of mock item data
"""

import factory
import pytest

from app.database.models.items import ItemInput


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
