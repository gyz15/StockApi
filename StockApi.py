import os
from dotenv import load_dotenv
import requests
load_dotenv()

API_KEY = os.getenv('ALPHAVANTAGE')
print(API_KEY)
