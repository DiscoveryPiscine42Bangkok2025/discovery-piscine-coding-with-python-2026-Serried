import sys as s
try:
    args = s.argv[1:]
    if len(args) > 0:
        print(f"parameters: {len(args)}")
        for i in args:
            print(f"{i}: {len(i)}")
    else:
        print("none")
except IndexError:
    print("none")