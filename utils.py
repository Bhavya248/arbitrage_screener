def get_unocoin_url(coin_name: str):
    if not coin_name:
        return None

    return f"https://api.unocoin.com/api/v1/exchange/orderbook?ticker_id={coin_name}_INR&depth=100"


def get_binance_url(coin_name: str):
    if not coin_name:
        return None

    return f"https://data-api.binance.vision/api/v3/ticker/price?symbol={coin_name}USDT"


def get_zebpay_url(coin_name: str):
    if not coin_name:
        return None

    return f"https://www.zebapi.com/api/v1/market/{coin_name}-INR/ticker"


def get_avg(num1, num2):
    if num1 and num2:
        return (float(num1) + float(num2)) / 2
    else:
        return None
