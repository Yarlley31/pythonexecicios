# Pedeindo para inserir o valor
num = int(input('Dgite um número para ver sua tabuada: '))
print('-=-' * 5)
# fazendo o laço de repetição
for n in range(1, 11):
    print(f'{num} x {n} = {num * n}')
print('-=-' * 5)
