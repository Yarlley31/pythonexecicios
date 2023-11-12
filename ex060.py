# from math import factorial PODE SE USAR A LIBARY
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

''' COMO EU FIZ QUE NÃO FICOU MT LEGAL
n = int(input('Digite um número calcular seu fatorial: '))
fatorial = 1
for i in range(1, n+1):
    fatorial *= i
print(f'O fatorial de {n} é {fatorial}')'''