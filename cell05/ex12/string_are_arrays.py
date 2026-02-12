import sys as s
try:
    args = s.argv[1]
    z = args.count("z")
    
    if z > 0:
        print("z" * z)
    else:
        print("none")
except IndexError:
    print("none")