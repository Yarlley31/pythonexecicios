print('-='*17)
print('Analisador de Triângulos')
print('-='*17)
r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
# A base do triangulo deve ser menor que a soma dos outros lados
if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('Será possível fazer um triângulo com essas retas!')
else:
    print('Não será possível fazer um triângulo com essas retas!')