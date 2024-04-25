mS = 0
fS = 0
fN = 0
mN = 0
amostra = 0

while amostra < 2000:
    opiniao = str(input('Digite se você gostou ou não do produto(S/N): '))
    if opiniao == 'S' or opiniao == 's':
        sexo = str(input('Digite seu sexo(M/F):'))
        if sexo == 'm' or sexo == 'M':
            mS += 1
        else:
            fS += 1
    else:
        sexo = str(input('Digite seu sexo(M/F):'))
        if sexo == 'm' or sexo == 'M':
            mN += 1
        else:
            fN += 1
    amostra += 1
print('Homens que gostaram foi: ', mS,'e mulheres que gostaram foi: ', fS, '\nHomens que não gostaram: ', mN, 'e mulheres que não gostaram: ', fN)