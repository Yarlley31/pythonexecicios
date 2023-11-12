# TEM ESSE JEITO COM O num FORA E DENTRO DO while. 
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
''' -> E DESSE JEITO COM O cont - 1 E soma - 999 QUE EU ENTENDI MAIS <-
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma += num
    cont += 1
print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma - 999}.')'''