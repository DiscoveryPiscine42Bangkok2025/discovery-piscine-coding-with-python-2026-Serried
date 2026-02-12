import sys as s
args = s.argv[1:]
if len(args) == 0:
    print("none")
else:
    for i in args:
        if i.endswith("ism"):
            continue
        else:
            print(i + "ism")