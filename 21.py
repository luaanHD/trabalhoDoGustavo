num = int(input('Digite seu número: '))
soma = 0
impar = 1

while soma < num:
    soma += impar
    impar += 2
if soma == num:
    print('Quadrado perfeito')
else:
    print('Não é quadrado perfeito')