
# stock_data.py

import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    return data['Adj Close']

def calculate_annual_returns(data):
    returns = data.pct_change().dropna()
    annual_returns = returns.mean() * 252
    return annual_returns

def calculate_covariance_matrix(data):
    returns = data.pct_change().dropna()
    covariance_matrix = returns.cov() * 252
    return covariance_matrix

# Example usage
if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOG']
    start_date = '2022-01-01'
    end_date = '2023-01-01'
    stock_data = fetch_stock_data(tickers, start_date, end_date)
    returns = calculate_annual_returns(stock_data)
    covariance_matrix = calculate_covariance_matrix(stock_data)

    print("Annual Returns:")
    print(returns)
    print("Covariance Matrix:")
    print(covariance_matrix)
 