N = 100
while N < 1000:
    c = N // 100
    d = N % 100 // 10
    u = N % 10
    if c < d < u:
        print(N, 'é um número ascendente')
    N += 1