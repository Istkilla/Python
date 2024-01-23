def palindrome():
    for x in range(999, 900, -1):
        for y in range(x, 900, -1):
            s = str(x*y)
            c = s [::-1]
            if s == c:
                return c
print(palindrome())
