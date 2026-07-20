# a = lambda x: x + 10
# print(a(5))  # Output: 15

# ............................

# x = lambda a, b: a * b
# print(x(5, 7))  # Output: 30

# ----- uning function with lambda -----
# def myfunc(n):
#     return lambda a : a * n

# double = myfunc(2)
# print(double(11))    

# ---------doubled-----------
# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda a: a * 2, numbers))
# print(doubled)  # Output: [2, 4, 6, 8, 10]

# -----odd---------
# odd_numbers = [1, 2, 3, 4, 5]
# odd = list(filter(lambda x: x % 2 != 0, odd_numbers))

# print(odd)  # Output: [1, 3, 5]


# ------sorted--------------
# students = [("Atik" ,25), ("Rafi" , 20), ("Sakib" , 22)]
# sort = sorted(students, key=lambda x : x[1])
# print(sort)  # Output: [('Rafi', 20), ('Sakib', 22), ('Atik', 25)]

# ----word-----
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['apple', 'cherry', 'banana']