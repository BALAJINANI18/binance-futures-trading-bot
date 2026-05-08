from datetime import datetime

import typer
from rich import print

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)

app = typer.Typer()


@app.command()
def place_order(
    symbol: str = typer.Argument(
        ...,
        help="Trading symbol. Example: BTCUSDT",
    ),

    side: str = typer.Argument(
        ...,
        help="Order side: BUY or SELL",
    ),

    order_type: str = typer.Argument(
        ...,
        help="Order type: MARKET or LIMIT",
    ),

    quantity: float = typer.Argument(
        ...,
        help="Quantity to trade",
    ),

    price: float = typer.Option(
        None,
        "--price",
        help="Price required for LIMIT orders",
    ),
):

    try:

        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        print(
            f"\n[bold yellow]Time:[/bold yellow] "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        print("\n[bold cyan]Order Summary[/bold cyan]")

        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if price:
            print(f"Price       : {price}")

        client = BinanceFuturesClient().get_client()

        order_manager = OrderManager(client)

        if order_type == "MARKET":

            response = order_manager.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
            )

        else:

            response = order_manager.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
            )

        print(
            "\n[bold green]"
            "SUCCESS: Order placed successfully"
            "[/bold green]"
        )

        print(
            f"Order ID       : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status         : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty   : "
            f"{response.get('executedQty')}"
        )

        print(
            f"Average Price  : "
            f"{response.get('avgPrice')}"
        )

    except Exception as error:

        print(
            "\n[bold red]"
            f"FAILED: {error}"
            "[/bold red]"
        )


if __name__ == "__main__":
    app()