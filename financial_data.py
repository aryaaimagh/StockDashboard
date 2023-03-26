import pandas as pd 
from api import get_income_statement

def get_income_statement_df(ticker):
    income_statement_data = get_income_statement(ticker)
    income_statement_df = pd.DataFrame(income_statement_data)
    income_statement_df['operatingIncomeRatio'] = income_statement_df['operatingIncomeRatio'].apply(lambda x: x * 100).round(2)
    income_statement_df['grossProfitRatio'] = income_statement_df['grossProfitRatio'].apply(lambda x: x * 100).round(2)
    return income_statement_df