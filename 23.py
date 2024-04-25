numero = int(input("Digite um número inteiro: "))

primo_anterior = numero - 1
while primo_anterior > 1:
    eh_primo = True
    for i in range(2, int(primo_anterior//2) + 1):
        if primo_anterior % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(f"O número primo mais próximo (menor que {numero}) é: {primo_anterior}")
        break
    primo_anterior -= 1