extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
            'doze', 'treze', 'quartoze', 'quinze', 'dezeseies', 'dezesete',
            'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'O numero {n} por extenso é {extenso[n]}')
    else:
        print('Número fora da faixa permitida! Tente novamente.')