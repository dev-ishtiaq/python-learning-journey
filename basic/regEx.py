import re

text = "The Earth moves around the Sun"

x = re.findall("Sun", text)
if x:
    print("yes found it")
else:
    print("not found")    