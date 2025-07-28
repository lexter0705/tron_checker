from tronpy.async_tron import AsyncTron, AsyncHTTPProvider

from tron.wallet_info import WalletInfo


class TronConnector:
    def __init__(self, endpoint_uri: str | dict = "https://api.trongrid.io", *args, **kwargs):
        provider = AsyncHTTPProvider(endpoint_uri, *args, **kwargs)
        self.__tron = AsyncTron(provider)

    async def get_wallet(self, address: str) -> WalletInfo:
        balance = await self.__tron.get_account_balance(address) / 1_000_000
        bandwidth = await self.__tron.get_bandwidth(address)
        energy = await self.__tron.get_energy(address)
        return WalletInfo(address=address, balance=balance, bandwidth=bandwidth, energy=energy)
