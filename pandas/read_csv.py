import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())


# ====== max_rows ============
print("-----------------------")

max = pd.options.display.max_rows
print(max)



# ====== change max_rows ============
print("-----------------------")

maxc = pd.options.display.max_rows = 9999
print(maxc)