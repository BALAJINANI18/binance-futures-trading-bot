import os

from binance.client import Client
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")


class BinanceFuturesClient:

    def __init__(self):

        api_key = os.getenv("BINANCE_API_KEY")
        secret_key = os.getenv("BINANCE_SECRET_KEY")


        self.client = Client(api_key, secret_key)

        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com/fapi"
        )

    def get_client(self):

        return self.client