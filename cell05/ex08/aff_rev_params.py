import sys as s
args = s.argv[1:]
if len(args) < 2:
    print("none")
    s.exit()
x= list(reversed(args))
for i in x:
    print(i)