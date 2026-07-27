import pandas as pd
df = pd.read_csv('data.csv')


# df.dropna(inplace = True)
# df.fillna(100, inplace = True)
# df.fillna({"Calories": 100}, inplace = True)


# x= df["Calories"].mean()
# df.fillna({"Calories" : x}, inplace= True)



# x= df["Calories"].median()
# df.fillna({"Calories" : x}, inplace= True)



x= df["Calories"].mode()[0]
df.fillna({"Calories" : x}, inplace= True)
print(df.to_string())
