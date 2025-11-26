import pandas as pd
import numpy as np
df = pd.read_csv('data/clean_nifty_50_historical_data_upto25-11.csv')
"""ADDING ADDITIONAL FEATURES"""
# Returns
df["Return"] = df["Close"].pct_change()
df["LogReturn"] = np.log(df["Close"]/df["Close"].shift(1))
df["HighLow"] = df["High"] - df["Low"]
df["CloseOpen"] = df["Close"] - df["Open"]
# TRENDS (MA)
df["MA20"] = df["Close"].rolling(20).mean()
df["MA40"] = df["Close"].rolling(40).mean()
# VOLATILITY
df["Volatility20"] = df["Return"].rolling(20).std()
df.to_csv('data/complete_nifty_50_historical_data_upto25-11.csv', index=False)
