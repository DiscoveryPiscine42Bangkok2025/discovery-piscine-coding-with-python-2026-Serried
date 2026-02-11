try:
    x = int(input("Give me a number: "))
    print("This numnber is an integer.")
except ValueError:
    print("This numnber is a decimal.")