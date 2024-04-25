n = 1000
while n <= 9999:
    q = n // 100
    r = n % 100
    if (q+r)**2 == n:
        print(n)
    n += 1