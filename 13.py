idade = 1
idadeMaior = 0

while idade != 0:
    idade = int(input('Digite a idade para saber qual a maior (Digite "0" para encerrar): '))
    if idade > idadeMaior:
        idadeMaior = idade
print('Idade maior: ', idadeMaior)
    