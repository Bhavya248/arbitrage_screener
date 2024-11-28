from dotenv import load_dotenv
import os

load_dotenv()

UNOCOIN_AUTH_TOKEN = os.getenv("UNOCOIN_AUTH_TOKEN")

COIN_PAIRS = ["XRP", "BCH", "LTC", "TRX", "DOGE", "XLM", "SOL"]

USDT_RATE = 90
