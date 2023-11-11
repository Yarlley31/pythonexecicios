num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1): # contar de até o valor do input
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='') 
    print(f'{c}', end=' ')
print(f'\nO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')