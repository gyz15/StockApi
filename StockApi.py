import os
from dotenv import load_dotenv
import requests
import time
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


stock_data = {
    'Symbol': 'TSLA',
    'AssetType': 'Common Stock',
    'Name': 'Tesla, Inc',
    'Description': 'Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, Netherlands, Norway, and internationally. The company operates in two segments, Automotive; and Energy Generation and Storage. The Automotive segment offers sedans and sport utility vehicles. It also provides electric powertrain components and systems; and services for electric vehicles through its company-owned service locations, and Tesla mobile service technicians, as well as sells used vehicles. This segment markets and sells its products through a network of company-owned stores and galleries, as well as through its own Website. The Energy Generation and Storage segment offers energy storage products, such as rechargeable lithium-ion battery systems for use in homes, industrial, commercial facilities, and utility grids; and designs, manufactures, installs, maintains, leases, and sells solar energy generation and energy storage products to residential and commercial customers. It also provides vehicle insurance services, as well as renewable energy. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was founded in 2003 and is headquartered in Palo Alto, California.', 'Exchange': 'NASDAQ', 'Currency': 'USD', 'Country': 'USA', 'Sector': 'Consumer Cyclical', 'Industry': 'Auto Manufacturers', 'Address': '3500 Deer Creek Road, Palo Alto, CA, United States, 94304', 'FullTimeEmployees': '48016', 'FiscalYearEnd': 'December', 'LatestQuarter': '2020-09-30', 'MarketCapitalization': '616002945024', 'EBITDA': '4019000064', 'PERatio': '1242.5621', 'PEGRatio': '1.4006', 'BookValue': '16.91', 'DividendPerShare': 'None', 'DividendYield': '0', 'EPS': '0.523', 'RevenuePerShareTTM': '30.668', 'ProfitMargin': '0.0197', 'OperatingMarginTTM': '0.0612', 'ReturnOnAssetsTTM': '0.0274', 'ReturnOnEquityTTM': '0.0559', 'RevenueTTM': '28175998976', 'GrossProfitTTM': '4069000000',
    'DilutedEPSTTM': '0.523', 'QuarterlyEarningsGrowthYOY': '0.694', 'QuarterlyRevenueGrowthYOY': '0.392', 'AnalystTargetPrice': '401.47', 'TrailingPE': '1242.5621',
    'ForwardPE': '172.4138', 'PriceToSalesRatioTTM': '25.1042', 'PriceToBookRatio': '41.0948', 'EVToRevenue': '23.4037', 'EVToEBITDA': '168.9962', 'Beta': '2.1512', '52WeekHigh': '695',
              '52WeekLow': '70.102', '50DayMovingAverage': '530.5347', '200DayMovingAverage': '387.1448', 'SharesOutstanding': '947900992', 'SharesFloat': '759514941', 'SharesShort': '46499466', 'SharesShortPriorMonth': '47898025', 'ShortRatio': '1.18', 'ShortPercentOutstanding': '0.05', 'ShortPercentFloat': '0.0612', 'PercentInsiders': '20.021', 'PercentInstitutions': '42.405', 'ForwardAnnualDividendRate': '0', 'ForwardAnnualDividendYield': '0', 'PayoutRatio': '0', 'DividendDate': 'None', 'ExDividendDate': 'None', 'LastSplitFactor': '5:1', 'LastSplitDate': '2020-08-31'}
# for key, value in stock_data.items():
#     print(f'''
#     --------------------------------------------------------------------------------------
#     {key}
#     {value}
#     --------------------------------------------------------------------------------------
#     '''
#           )

# todo cashflow & cagr
# print({} == {})


def get_cash_flow(symbol, api_key):
    # todo wait if get
    net_income = []
    fiscal_date_ending = []
    free_cash_flow = []
    data = requests.get(
        f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={api_key}").json()
    if "Note" in data.keys():
        time.sleep(60)
    else:
        for i in range(3):
            fiscal_date_ending.append(
                data['annualReports'][i]['fiscalDateEnding'])
            net_income.append(int(data['annualReports'][i]['netIncome']))
            free_cash_flow.append(int(data['annualReports'][i]['operatingCashflow'])-int(
                data['annualReports'][i]['capitalExpenditures']))
        return {"fiscal_date_ending": fiscal_date_ending, "net_income": net_income, "free_cash_flow": free_cash_flow}


print(get_cash_flow('tsla', API_KEY))
