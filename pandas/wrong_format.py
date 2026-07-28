import pandas as pd

df = pd.read_csv('data_with_dates.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())



# df.dropna(subset=['Date'], inplace = True)

# print(df.to_string())