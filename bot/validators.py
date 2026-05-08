from bot.exceptions import ValidationError


VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol: str):

    if not symbol.endswith("USDT"):
        raise ValidationError(
            "Symbol must end with USDT"
        )


def validate_side(side: str):

    if side.upper() not in VALID_SIDES:
        raise ValidationError(
            "Side must be BUY or SELL"
        )


def validate_order_type(order_type: str):

    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValidationError(
            "Order type must be MARKET or LIMIT"
        )


def validate_quantity(quantity: float):

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than zero"
        )


def validate_price(price, order_type: str):

    if order_type.upper() == "LIMIT":

        if price is None:
            raise ValidationError(
                "Price is required for LIMIT orders"
            )

        if price <= 0:
            raise ValidationError(
                "Price must be greater than zero"
            )