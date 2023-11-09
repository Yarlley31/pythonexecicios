n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 + n2 + n3) / 3
print(f'Tirando {n1:.1f}, {n2:.1f} e {n3:.1f}, a média do aluno é {media:.1f}')
if media < 5:
    print('O aluno está REPROVADO.')
elif 7 > media >= 5:
    print("O aluno está em RECUPERAÇÃO.")
else:
    print('O aluno está APROVADO.')
print('Bom estudos!')