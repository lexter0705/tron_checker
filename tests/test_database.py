import pytest
from httpx import AsyncClient, ASGITransport

from main import app


@pytest.mark.asyncio
async def test_database():
    async with AsyncClient(transport=ASGITransport(app),
                           base_url="http://test") as client:
        await client.post("/get_wallet_info", json={"address": "TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N"})
        database_response = await client.get("/get_data")
        id_before = database_response.json()[-1]["id"]
        response = await client.post("/get_wallet_info", json={"address": "TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N"})
        database_response = await client.get("/get_data")
        assert response.status_code == 200
        assert len(database_response.json()) > 0
        assert id_before != database_response.json()[-1]["id"]
        assert database_response.json()[-1]["address"] == response.json()["address"]
