import sys as s
args = s.argv[1:3]
a = []
if args:
    for i in range(int(args[0]), int(args[1])+1):
        a.append(i)
    print(a)
else:
    print("none")