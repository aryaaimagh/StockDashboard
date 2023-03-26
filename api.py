import requests
from config import API_KEY


def get_income_statement(ticker):
    url = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?apikey={API_KEY}"
    response = requests.get(url)
    income_statement_data = response.json()
    return income_statement_data