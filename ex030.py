num = int(input('Insira um número e lhe direi se ele é PAR ou IMPAR: '))
par = num% 2
if par == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é IMPAR')
