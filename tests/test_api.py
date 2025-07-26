import pytest
from httpx import AsyncClient, ASGITransport

from main import app
from tron import WalletInfo


@pytest.mark.asyncio
async def test_api():
    async with AsyncClient(transport=ASGITransport(app),
                           base_url="http://test") as client:
        response = await client.post("/get_wallet_info", json={"address": "TT2T17KZhoDu47i2E4FWxfG79zdkEWkU9N"})
        assert response.status_code == 200
        assert isinstance(WalletInfo.model_validate(response.json()), WalletInfo)
        response = await client.post("/get_wallet_info", json={"address": "TE2RzoSV3wFK99w6J9UnnZ4vLfXYoxvAAA"})
        assert response.status_code == 422
        assert response.json() == {"detail": "bad address"}
