from binance.exceptions import BinanceAPIException

from bot.logging_config import setup_logger


logger = setup_logger()


class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_market_order(
        self,
        symbol,
        side,
        quantity,
    ):

        try:

            logger.info(
                f"MARKET ORDER | "
                f"Symbol={symbol} "
                f"Side={side} "
                f"Quantity={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )

            logger.info(
                f"Market order success: {response}"
            )

            return response

        except BinanceAPIException as error:

            logger.error(
                f"Binance API Error: {error}"
            )

            raise

        except Exception as error:

            logger.error(
                f"Unexpected Error: {error}"
            )

            raise

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price,
    ):

        try:

            logger.info(
                f"LIMIT ORDER | "
                f"Symbol={symbol} "
                f"Side={side} "
                f"Quantity={quantity} "
                f"Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

            logger.info(
                f"Limit order success: {response}"
            )

            return response

        except BinanceAPIException as error:

            logger.error(
                f"Binance API Error: {error}"
            )

            raise

        except Exception as error:

            logger.error(
                f"Unexpected Error: {error}"
            )

            raise