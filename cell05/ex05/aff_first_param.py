import sys as s
args = s.argv[1:]
for i in args:
    if type(i) == type(""):
        print(i)
        s.exit()
print("none")