f1, f2, c = 0, 1, 0
while f2 <= 4000000:
    c = c + f2 if f2 % 2 == 0 else c
    f1, f2 = f2, f1 + f2
print(c)
