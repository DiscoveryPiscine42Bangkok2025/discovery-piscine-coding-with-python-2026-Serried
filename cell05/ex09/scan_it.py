import sys as s
args = s.argv[1:3]
if len(args) < 2:
    print("none")
else:
    print(f"{args[1].count(args[0])}")