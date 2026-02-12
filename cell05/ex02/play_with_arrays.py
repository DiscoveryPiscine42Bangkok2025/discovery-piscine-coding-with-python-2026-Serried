original = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
print(f"Original array: {original}")
for i in original:
    if i > 5:
        new.append(i+2)
print(f"New array: {new}")