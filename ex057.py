sexo = str(input('Digite o sexo da pessoa: [F/M] ')).upper().strip()[0]
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Você não digitou o sexo corretamente, digite novamente: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso')