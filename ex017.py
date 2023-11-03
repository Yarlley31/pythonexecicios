from math import hypot
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')

'''catop = float(input('Informe o comprimento do cateto oposto: '))
catadj = float(input('Informe o comprimento do cateto adjacente: '))
hipo = (catop**2 + catadj**2) ** (1/2)
print(f'O comprimento da hipotenusa é: {hipo:.2f}')'''