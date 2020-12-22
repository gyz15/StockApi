import os
from dotenv import load_dotenv
import requests
load_dotenv()

API_KEY = os.getenv('ALPHAVANTAGE')

CHECK_TYPE = (
    "OVERVIEW",
    "INCOME_STATEMENT",
    "BALANCE_SHEET",
    "CASH_FLOW",
    "EARNINGS",
    "LISTING_STATUS",
)


def get_stock(name, check_type, api_key):
    data = requests.get(
        f"https://www.alphavantage.co/query?function={check_type}&symbol={name}&apikey={api_key}")
    return data.json()


stock_data = get_stock("TSLA", CHECK_TYPE[0], API_KEY)
print(stock_data)
print(type(stock_data))
