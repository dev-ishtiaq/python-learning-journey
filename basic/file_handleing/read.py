# f = open("demo.txt")
# print(f.read())



# ---------with---------------
# with open("demo.txt") as f:
#     print(f.read())

# --line----
# f = open("demo.txt")
# print(f.readline())
# f.close()


# with open("demo.txt") as f:
#   for x in f:
#     print(x)


# ---------add text------

# with open("newfile.txt", "a") as f:
#     f.write("here is txt")

# with open("newfile.txt") as f:
#     print(f.read())


# ---------overwrite text------

with open("newfile.txt", "w") as f:
    f.write("text removed")

with open("newfile.txt") as f:
    print(f.read())



    
with open("newfile.txt", "a") as f:
    f.write("here is txt")

with open("newfile.txt") as f:
    print(f.read())



