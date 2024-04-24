p = float(input('Digite a quantidade de kg de peixe pescado: '))

if p > 50:
    #dif = p - 50
    total = (p-50) * 4
    print('O total a pagar de multa é: R$', total)
else:
    print('Você não excedeu o limite, por isso não será multado')