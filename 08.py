n = int(input('Digite um numero inteiro: '))
soma = 0
i = 1
if n > 0:
    while i <= n:
        soma += 1 / i
        i+=1
    print('A quantidade solicitada foi:', n, 'e o valor da soma foi', soma)
else:
    print('Número inválido')