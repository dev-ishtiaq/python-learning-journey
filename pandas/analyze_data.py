import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())


# ======= show tail rows =========
print("------------------------------------")
print(df.tail())

# ======= info =========
print("------------------------------------")
print(df.info())