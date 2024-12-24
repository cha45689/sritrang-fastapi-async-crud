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
from app.database.models.items import Item
from app.database.models.pagination import Pagination
from tests.integration.conftest import IDStorage
from tests.mock_data.item import (  # noqa: F401; pylint: disable=W0611
    ItemInputFactory,
    invalid_item_input,
    valid_item_input,
)


@pytest_asyncio.fixture(name="client", scope="session")
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
async def test_read_no_result(client):
    """
    Test GET method of items routes to get all items when there is no record
    """
    response = await client.get(
        "/api/v1/items/", params={"page": 9999, "size": 999999, "desc": True}
    )
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_create(client, valid_item_input):  # noqa: F811; pylint: disable=W0621
    """
    Test success POST method of items routes aka create item
    """
    response = await client.post("/api/v1/items/", json=valid_item_input.model_dump())
    assert response.status_code == 200
    if response.status_code == 200:
        json_response = response.json()
        IDStorage.item_id = json_response.pop("id")
        logging.info("Item ID : %s", IDStorage.item_id)
        assert json_response == valid_item_input.model_dump()


@pytest.mark.asyncio
async def test_fail_create_validation_error(client):
    """
    Test fail POST method due to validation
    """
    response = await client.post("/api/v1/items/", json=invalid_item_input[0])
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_read(client):
    """
    Test GET method of items routes aka read item by id
    """
    response = await client.get(f"/api/v1/items/{IDStorage.item_id}")
    assert response.status_code == 200
    item = Item(**response.json())
    assert item.id == IDStorage.item_id


@pytest.mark.asyncio
async def test_read_all(client):
    """
    Test GET method of items routes to get all items using pagination
    """
    response = await client.get(
        "/api/v1/items/", params={"page": 1, "size": 10, "desc": True}
    )
    assert response.status_code == 200
    json_response = response.json()
    assert "data" in json_response
    assert "pagination" in json_response
    assert isinstance(json_response["data"], list)
    Pagination(**json_response["pagination"])


@pytest.mark.asyncio
async def test_read_page_exceed(client):
    """
    Test GET method of items routes to get all items using pagination in case page exceed last page
    hopefully no one will seed test database with more than the 999999*9999 record
    """
    response = await client.get(
        "/api/v1/items/", params={"page": 9999, "size": 999999, "desc": True}
    )
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update(client):
    """
    Test PUT method of items routes aka update item
    """
    update_input = ItemInputFactory.build()
    response = await client.put(
        f"/api/v1/items/{IDStorage.item_id}", json=update_input.model_dump()
    )
    assert response.status_code == 200
    item = Item(**response.json())
    assert item.id == IDStorage.item_id


@pytest.mark.asyncio
async def test_delete(client):
    """
    Test DELETE method of items routes
    """
    response = await client.delete(f"/api/v1/items/{IDStorage.item_id}")
    assert response.status_code == 200
    item = Item(**response.json())
    assert item.id == IDStorage.item_id


@pytest.mark.parametrize("method", ["GET", "PUT", "DELETE"])
@pytest.mark.asyncio
async def test_not_found(
    client, method, valid_item_input  # noqa: F811; pylint: disable=W0621,W0613
):
    """
    Test item not found cases for all method
    """
    response = await client.request(
        method=method, url=f"/api/v1/items/{IDStorage.item_id}"
    )
    assert response.status_code == 404
