import pandas as pd

a = [1,3,7]

myvar = pd.Series(a)
print(myvar)


# ----Create Labels------
var2 = pd.Series(a, index = ["x","y","z"])
print(var2)


food = {"day1": 670, "day2": 560, "day3": 800}

v3 = pd.Series(food)

print(v3)


v4 = pd.Series(food, index = ["day1", "day2"])
print(v4)