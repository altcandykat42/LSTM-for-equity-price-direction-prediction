import yfinance as yf
from datetime import datetime as datetime
import pandas as pd
import os
TICKER = "^NSEI"

def end_start_dates():
    now = datetime.now()
    end = datetime(now.year, now.month, now.day+1)
    start = datetime(now.year-20, now.month, now.day)
    return start, end

def ticker_to_df(ticker):
    start, end = end_start_dates()
    stock_data = yf.download(ticker, start=start, end=end)
    df = pd.DataFrame(stock_data)
    return df

def store_data_to_csv(data, filename):
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename+'.csv')
    data.to_csv(output_path, index=True)

df = ticker_to_df(ticker=TICKER)
store_data_to_csv(data=df, filename="nifty_50_historical_data")

