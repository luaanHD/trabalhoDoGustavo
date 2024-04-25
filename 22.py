for N in range(1, 1001):
    for d in range(2, N // 2 + 1):
        if N % d == 0:
            break
    else:
        print(f'{N} é um número primo')