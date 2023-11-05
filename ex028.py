import random
from time import sleep
print('-=-' * 16)
print('Bem-vindo ao jogo da adivinhação!')
print('-=-' * 16)
num = int(input('Pensei em um número de 0 a 5, adivinhe qual é: ')) # Aqui o jogador tenta adivinhar
resposta = random.randrange(5) # Faz o computador "PENSAR"
print('PROCESSANDO...')
sleep(1)
if num == resposta:
    print('PARABÉNS você acertou, vamos jogar de novo?')
else:
    print(f'Que pena não foi dessa vez, pensei no número {resposta}')




'''print('Vamos brincar de "Adivinhe o Número"!')
num = 4
print('Pensei em um número entre 0 e 5')
n = int(input('Agora adivinhe!: '))
if n == 2:
    print(f'Você acertou!')
else:
    print(f'Você errou! O número era ')'''