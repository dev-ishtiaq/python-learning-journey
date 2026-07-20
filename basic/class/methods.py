# class person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello this is " + self.name)    

# pn = person("Ishti")

# pn.greet()


# -------Methods with Parameters-------

# class cal:
#     def add(self, a ,b):
#         return a + b

#     def mul(self, a, b):
#         return a * b

# c = cal()
# print(c.add(5,7))
# print(c.mul(6,7))


# ----Methods Accessing Properties-------

# class student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

#     def info(self):
#         return f"{self.name} roll no {self.roll}" 

# st = student("Nayem", 5)
# print(st.info())


class birth:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate(self):
        self.age += 1
        print(f"Happy BD {self.name}. your're now {self.age} years old")


b = birth("Ishtiaq", 27)
b.celebrate()
b.celebrate()
