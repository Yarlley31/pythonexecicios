n = soma = cont = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles é {soma}')