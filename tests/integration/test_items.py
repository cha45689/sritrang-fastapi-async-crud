"""
This module is use to store integration test code for items route
under path api/v1/items
"""

import logging

import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

from app.application.main import app
from tests.integration.conftest import IDStorage
from tests.mock_data.item import (  # noqa: F401; pylint: disable=W0611
    invalid_item_input,
    valid_item_input,
)


@pytest_asyncio.fixture(name="client")
async def async_client():
    """
    fixture for async test client of items
    """
    async with LifespanManager(app) as manager:
        async with AsyncClient(
            transport=ASGITransport(app=manager.app), base_url="http://test"
        ) as ac:
            yield ac


@pytest.mark.asyncio
async def test_create(client, valid_item_input):  # noqa: F811; pylint: disable=W0621
    """
    Test success POST method of items routes aka create item
    """
    response = await client.post("/api/v1/items/", json=valid_item_input.model_dump())
    assert response.status_code == 200
    if response.status_code == 200:
        IDStorage.item_id = response.json()["id"]
        logging.info("Item ID : %s", IDStorage.item_id)


@pytest.mark.asyncio
async def test_fail_create_validation_error(client):  # pylint: disable=W0613
    """
    Test fail POST method due to validation
    """
    response = await async_client.post("/api/v1/items/", json=invalid_item_input[0])
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_read(client):  # pylint: disable=W0613
    """
    Test GET method of items routes aka read item
    """


@pytest.mark.asyncio
async def test_read_all(client):  # pylint: disable=W0613
    """
    Test GET method of items routes aka read item
    """


@pytest.mark.asyncio
async def test_update(client):  # pylint: disable=W0613
    """
    Test PUT method of items routes aka update item
    """


@pytest.mark.asyncio
async def test_delete(client):  # pylint: disable=W0613
    """
    Test DELETE method of items routes
    """
