salario = float(input('Qual é o seu salário atual? R$'))
if salario > 1250:
    aumento = salario * (10/100)
    novo = salario + aumento
    print(f'Seu novo salário é R${novo:.2f}')
else:
    novo2 = salario + (salario * 15/100)
    print(f'Seu novo salário é R${novo2:.2f}')
