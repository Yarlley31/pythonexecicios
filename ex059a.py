n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''        [ 1 ] somar
        [ 2 ] multiplicação
        [ 3 ] maior
        [ 4 ] novos númeoros
        [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é igaul a {produto} ')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os núemros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')