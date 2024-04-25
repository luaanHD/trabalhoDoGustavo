ano = int(input('Digite o ano atual: '))
for ano in range(1, ano+1):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(ano)