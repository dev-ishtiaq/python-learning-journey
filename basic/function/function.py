# -----------args-------------
# def num_func(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(num_func(10,15))









# ------------args/kwargs------------------
# def function(**child):
#     print("My Clild First Name is " + child['lname'])
# function(fname = "Emil", lname = "Refat")

# def datafunc(**mydata):
#     print("data type is ", type(mydata))
#     print("developer name is " + mydata['name'])
#     print("his age " + mydata['age'])
#     print(mydata)

# datafunc(name = "Refat", age = "25", country = "Bangladesh")

# -regular arguments -
# def regular_func(username, **vars):
#     print("username: " + username)
#     for key, value in vars.items():
#         print(" " , key + ": " ,  value)
   
# regular_func("ahmed28", name = "Ishtiaq", experience = "2 years")

# --combined args and kwargs--
# def com_func(title, *args, **kwargs):
#     print("Title: " + title)
#     print("args: ", args)
#     print("kwargs: ", kwargs)   
# com_func("My Title", "arg1", "arg2", key1="value1", key2="value2")

# --unpacking numbers in args -
# def unpack_func(a, b, c):
#     return(a + b + c)

# numbers = (1, 2, 3)
# result = unpack_func(*numbers)
# print(result)

# --unpacking dictionary in kwargs --
# def unpack_dict_func(name, age, country):
#     print("Name: " + name)
#     print("Age: " + str(age))
#     print("Country: " + country)

# person = {"name": "Refat", "age": 25, "country": "Bangladesh"}
# unpack_dict_func(**person)











