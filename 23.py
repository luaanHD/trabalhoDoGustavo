N = int(input('Digite um número inteiro: '))

# Encontrando o número primo mais próximo anterior
primo_anterior = N - 1
while primo_anterior > 1:
    eh_primo = True
    for i in range(2, primo_anterior):
        if primo_anterior % i == 0:
            eh_primo = False
            break
    if eh_primo:
        break
    primo_anterior -= 1

# Encontrando o número primo mais próximo posterior
primo_posterior = N + 1
while True:
    eh_primo = True
    for i in range(2, primo_posterior):
        if primo_posterior % i == 0:
            eh_primo = False
            break
    if eh_primo:
        break
    primo_posterior += 1

# Verificando qual é o primo mais próximo e imprimindo
if N - primo_anterior <= primo_posterior - N:
    print(f"O número primo mais próximo de {N} é: {primo_anterior}")
else:
    print(f"O número primo mais próximo de {N} é: {primo_posterior}")