import sys as s
try:
    args = s.argv[1]
    check = input("What was the parameter? ")
    if check == args:
        print("Good job!")
    else:
        print("Nope, sorry...")
except IndexError:
    print("none")
    