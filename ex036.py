casa = float(input('Valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Quantos anos de finaciamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 /100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de {prestação:.2f}')
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print("Empréstimo NEgado!")