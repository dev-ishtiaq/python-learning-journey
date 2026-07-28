import pandas as pd

df = pd.read_csv('data.csv')

# df.loc[5, 'Duration'] = 80

# print(df.to_string())


# for x in df.index:
#     if df.loc[x, 'Duration'] > 50:
#         df.loc[x, 'Duration'] = 50


for x in df.index:
    if df.loc[x, 'Duration'] > 50:
        df.drop(x, inplace = True)


print(df.to_string())       