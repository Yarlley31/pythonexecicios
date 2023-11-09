r1 = int(input('Primeiro lado: '))
r2 = int(input('Segundo lado: '))
r3 = int(input('Terceiro lado: '))
if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('Os segmentos acima podem formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima não podem formar um triângulo')