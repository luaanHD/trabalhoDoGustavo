N = int(input('Informe a quantidade de termos da sequencia de Fibonacci -> '))
i = 1
a = 0
b = 1
print('1')
while i < N:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1