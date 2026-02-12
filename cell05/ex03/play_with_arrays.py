original = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
print(f"{original}")
for i in original:
    if i > 5:
        new.append(i+2)
new = list(set(new))
print(f"{new}")