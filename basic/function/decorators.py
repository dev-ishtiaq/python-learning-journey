# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myname():
#     return "Hello Dear"
# print(myname())

# ------------------------------------

# def changecase(func):
#     def inner(a):
#         return func(a).upper()
#     return inner

# @changecase
# def myfunc(name):
#     return "Hello! dear " + name
# print(myfunc("Refat"))        

# --------------------------------------

# -----Decorator With Arguments-------

# def changecase(n):
#     def changecase(func):
#         def inner():
#             if n >= 1:
#                 a = func().upper()
#             else:
#                 a = func().lower()
#             return a
#         return inner
#     return changecase

# @changecase(0) 
# def myname():
#     return "Hello! dear ishtiaq Ahmed"

# print(myname())



# ---Multiple Decorators---

def changecase(func):
    def inner():
        return func().upper()
    return inner

def addname(func):
    def inner():
        return "Hello! " + func() + " How are you?"
    return inner

@changecase
@addname
def name():
    return "Refat"
print(name())    