n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('''Escolha umas das opções abaixo para executar no programa: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 4 ] sair do programa''')
opção = int(input('Sua opção: '))
if opção == 1:
    resposta = n1 + n2 
    print(f'A soma de {n1} + {n2} = {resposta}')
elif opção == 2:
    resposta = n1 * n2
    print(f'A multiplicação de {n1} x {n2} = {resposta}')
elif opção == 3:
    if n1 > n2:
        print(f'O maior núemro é {n1}')
    else:
        print(f'O maior número é {n2}')
elif opção == 4:
    while opção == 4:
        n1 = int(input('Digite os novos números: '))
        n2 = int(input('Digite novamente outro novo número: '))
        print('''Escolha umas das opções abaixo executar no programa: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 4 ] sair do programa''')
        opção = int(input('Sua opção: '))
        if opção == 1:
            resposta = n1 + n2
            print(f'A soma de {n1} + {n2} = {resposta}')
        elif opção == 2:
            resposta = n1 * n2
            print(f'A multiplicação de {n1} x {n2} = {resposta}')
        elif opção == 3:
            if n1 > n2:
                print(f'O maior número é {n1}')
            else:
                print(f'O maior núemro é {n2}')
else:
    print('Você encerrou o programa')