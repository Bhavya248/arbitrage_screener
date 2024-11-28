from dotenv import load_dotenv
import os

load_dotenv()

UNOCOIN_AUTH_TOKEN = os.getenv("UNOCOIN_AUTH_TOKEN")

COIN_PAIRS = {
    "XRP": {"UNOCOIN": "XRP_INR", "BINANCE": "XRPUSDT"},
    "BCH": {"UNOCOIN": "BCH_INR", "BINANCE": "BCHUSDT"},
    "LTC": {"UNOCOIN": "LTC_INR", "BINANCE": "LTCUSDT"},
    "TRX": {"UNOCOIN": "TRX_INR", "BINANCE": "TRXUSDT"},
    "DOGE": {"UNOCOIN": "DOGE_INR", "BINANCE": "DOGEUSDT"},
    "XLM": {"UNOCOIN": "XLM_INR", "BINANCE": "XLMUSDT"},
    "SOL": {"UNOCOIN": "SOL_INR", "BINANCE": "SOLUSDT"},
}

USDT_RATE = 90