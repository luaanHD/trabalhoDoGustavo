voto = 1
votoTotal = 0
dilma = 0
aecio = 0
marina = 0
nulo = 0
while voto != 0:
    voto = int(input('Digite o número do seu candidato(0 para encerrar):'))
    if voto == 13:
        dilma += 1
        votoTotal += 1
    elif voto == 45:
        aecio += 1
        votoTotal += 1
    elif voto == 43:
        marina += 1
        votoTotal += 1
    elif voto != 0:
        nulo += 1
        votoTotal += 1
porcetagemDilma = (dilma * 100) / votoTotal
porcetagemAecio = (aecio * 100) / votoTotal
porcetagemMarina = (marina * 100) / votoTotal
if dilma > aecio and dilma > marina:
    print('Total:',votoTotal, 'Dilma:',dilma, 'Aécio:',aecio, 'Marina:',marina, 'Nulos:',nulo, '\nDilma ganhou com', porcetagemDilma, '% dos votos totais')
elif aecio > dilma and aecio > marina:
    print('Total:',votoTotal, 'Dilma:',dilma, 'Aécio:',aecio, 'Marina:',marina, 'Nulos:',nulo, '\nAécio ganhou com', porcetagemAecio, '% dos votos totais')
else:
    print('Total:',votoTotal, 'Dilma:',dilma, 'Aécio:',aecio, 'Marina:',marina, 'Nulos:',nulo, '\nMarina ganhou com', porcetagemMarina, '% dos votos totais')
