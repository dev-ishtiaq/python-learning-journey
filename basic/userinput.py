# print("What is your name?")
# name = input()
# print(f"hello {name}")
# fav1 = input("what is your location? ")
# fav2 = input("what are you looking for? ")
# fav3 = input("when you need this? ")

# print(f"Yes! we found a {fav2} at {fav1} in {fav3}")

import math
# ------calculation----------
# x = input("enter a number:")

# y = math.sqrt(float(x))

# print(f"the sqare root of {x} is {y}")


a = True
while a == True:
    b = input("Enter a numer:")
    try:
        b = float(b);
        a = False
    except:
        print("wrong input")
print("thanks")            