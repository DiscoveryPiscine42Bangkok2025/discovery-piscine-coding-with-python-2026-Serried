import sys as s
x = input("What you gotta say? : ")
if x == "STOP":
    s.exit()
while True:
    x = input("I got that! Anything else ? : ")
    if x == "STOP":
        break