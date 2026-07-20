# price = 40
# txt = f"The price is {price:.2f} taka"
# print(txt)

# price = 400000
# txt = f"The price is {price:,} taka"
# print(txt)

# price = 40
# tax = 5
# txt = f"The price is {price*tax} taka"
# print(txt)


# price = 5

# txt = f"The price is {'Low' if price<10 else 'High'} "
# print(txt)


# car = "toyota"

# p = f"my car brand is {car.upper()}"

# print(p)



# -------unsing format()--------------
# price = 40
# txt = "the price is {} taka"
# print(txt.format(price))


# price = 409999
# txt = "the price is {:,} taka"
# print(txt.format(price))


# ------multiple-----
# qty = 4
# product = "pen"
# price = 30

# order = "I need {} {}, price {} taka"

# print(order.format(qty,product,price))

# ------index-----
qty = 4
product = "pen"
price = 30

order = "I need {0} {1}, price {2} taka"

print(order.format(qty,product,price))
