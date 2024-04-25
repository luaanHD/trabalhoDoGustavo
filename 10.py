cont = 0
mediaMaior = 0
mediaMenor = 10  

while cont < 4:
    media1 = float(input('Digite a média do aluno: '))
    if 0 <= media1 <= 10:  
        if media1 > mediaMaior:
            mediaMaior = media1
        if media1 < mediaMenor:
            mediaMenor = media1
    else:
        print('Média inválida')
    cont += 1

print('Com base nas médias digitadas, a maior foi ->', mediaMaior, 'e a menor ->', mediaMenor)

