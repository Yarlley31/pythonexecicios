
preço = float(input('Preço das compras: R$'))
print('''Escolha uma das formas de pagamento abaixo: 
[ 1 ] dinheiro/cheque
[ 2 ] cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Sua opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print(f'Pagando à vista você recebe 10% de desconto, o novo valor ficará R${total:.2f}')
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print(f'Pagando à vista no cartão você recebe 5% de desconto, o novo valor será R${total:.2f}')
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f"Sua compra será percelada em {totparc}x de R${parcela:.2f} COM JUROS")
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua comprar de R${preço:.2f} vai custar R${total:.2f} no final.')