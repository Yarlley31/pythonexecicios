from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano em que você nasceu: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} para o alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}.')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo}')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')