from random import shuffle
n1 = input('Primeiro aluno(a): ')
n2 = input('Segundo aluno(a): ')
n3 = input('Terceiro aluno(a): ')
n4 = input('Quarto aluno(a): ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresenção será:')
print(lista)
