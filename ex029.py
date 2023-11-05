velocidade = int(input('Qual foi a volocidade do carro? '))

if velocidade > 80:
    print('Você está multado por exesso de velocidade!')
    n1 = velocidade - 80
    multa = n1 * 7
    # poderia ser tambem:
    # multa = (velocidade - 80) * 7
    print(f'O valor da sua multa é R${multa}.')
print('Tenha um bom dia e diriga com cuidado!')