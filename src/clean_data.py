import pandas as pd
import numpy as np
df = pd.read_csv('data/nifty_50_historical_data.csv')
clean_dih = df.drop(index=[0,1]).copy()
clean_dih.rename(columns={'Price':'Date'}, inplace=True)
clean_dih['Date'] = pd.to_datetime(clean_dih['Date'], dayfirst=True)
date_filter = clean_dih['Date']>=pd.Timestamp('2009-01-01')
clean_dih = clean_dih[date_filter]
print(clean_dih.info())
df["Return"] = df["Close"].pct_change(fill_method='bfill')
print(clean_dih.head())
# df["LogReturn"] = np.log(df["Close"]/df["Close"].shift(1))
# df["HighLow"] = df["High"] - df["Low"]
# df["CloseOpen"] = df["Close"] - df["Open"]
# # TRENDS (MA)
# df["MA20"] = df["Close"].rolling(20).mean()
# df["MA40"] = df["Close"].rolling(40).mean()
# # VOLATILITY
# df["Volatility20"] = df["Return"].rolling(20).std()
# date_filter = clean_dih['Date']>=pd.Timestamp('2010-01-01')
# clean_dih = clean_dih[date_filter]
# clean_dih = clean_dih.reset_index(drop=True)
# clean_dih.to_csv('data/clean_nifty_50_historical_data_upto25-11.csv', index=False)