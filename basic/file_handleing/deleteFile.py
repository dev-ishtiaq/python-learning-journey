import os

if os.path.exists("ex.txt"):  
    os.remove("ex.txt")
    print("file removed")
else:
    print("file dosent exists")


