import pandas as pd

data = {
    "cal": [450, 327, 670],
    "du": [6, 8, 9]
}

df = pd.DataFrame(data)
print(df)
print("-------------------")
print(df.loc[[0,1]])


#=== index rename  ======
df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print("-------------------")
print(df2)
print("-------------------")
print(df2.loc["day1"])



