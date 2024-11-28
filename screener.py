from config import COIN_PAIRS, USDT_RATE
from utils import get_unocoin_url, get_binance_url, get_avg
import requests, json


def find_arbitrage_opportunities():
    global COIN_PAIRS
    for coin in COIN_PAIRS:
        # get UNOCOIN orderbook
        unocoin_ob = json.loads(
            requests.request(
                "GET", get_unocoin_url(COIN_PAIRS[coin].get("UNOCOIN"))
            ).text
        )["asks"]

        # get Binance Price
        binance_price = json.loads(
            requests.get(get_binance_url(COIN_PAIRS[coin].get("BINANCE"))).text
        )

        # compare difference between coin prices
        difference = get_avg(unocoin_ob[0][0], unocoin_ob[1][0]) / float(
            binance_price["price"]
        )

        print("difference: " + str(difference))

        available_qty = unocoin_ob[0][1] + unocoin_ob[1][1]

        diff_in_percent = ((USDT_RATE - difference) / USDT_RATE) * 100
        print(f"coin: {coin}")
        print(f"diff: {diff_in_percent}")
        print(f"available qty: {available_qty}")
        print("\n\n")


find_arbitrage_opportunities()
