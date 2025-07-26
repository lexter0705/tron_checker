from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from tronpy.exceptions import BadAddress, AddressNotFound

from api.models import Address, RequestInfo
from config import get_config
from database import RequestWorker, RequestTable
from tron import TronConnector, WalletInfo

router = APIRouter()

config = get_config()
database_worker = RequestWorker(config.database_url)

tron_connector = TronConnector(config.tron_api_endpoint, api_key=config.tron_api_key)


@router.post("/get_wallet_info")
async def get_wallet_info(address: Address, request: Request) -> WalletInfo:
    database_worker.add_request(
        RequestTable(ip_address=request.client.host, port=request.client.port, tron_address=address.address))
    try:
        wallet_info = await tron_connector.get_wallet(address.address)
    except AddressNotFound:
        raise HTTPException(422, "bad address")
    except BadAddress:
        raise HTTPException(422, "bad address")
    except Exception as e:
        raise HTTPException(500, str(e))
    return wallet_info


@router.get("/get_data")
async def get_data_from_database() -> list[RequestInfo]:
    data = database_worker.get_last_rows(5)
    return [RequestInfo(id=i.id, ip_address=i.ip_address, address=i.tron_address, port=i.port) for i in data]
