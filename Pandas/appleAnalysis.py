import os
import xlrd
import pandas as pd

#we can re used this variable used your own drive path where u save these files
path = "C:\Users\haide\code\PythonBootCamp\Pandas"

df = pd.read_csv(path + "\\apple.csv", index_col='Date', parse_dates=True)
#print(df)

# df = df.sort_index()
# print(df.info())

# #calculate mean closing price in 2013:
# df_mean = df.loc['2013-Feb', 'Close'].mean()
# print(df_mean)

# #calculate mean closing price in 2012:
# df_mean = df.loc['2013-Feb', 'Close'].mean()
# print(df_mean)

# #specific time period
# df_spec =  df.loc['2012-Feb':'2015-Feb', 'Close'].mean()
# print(df_spec)

#Do you want to know a mean of closing price by weeks? No prob.
# we user here "W" you may see more aliases here
# http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases

df_week  = df.resample('W')['Close'].mean()
print(df_week)

