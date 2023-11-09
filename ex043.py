peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura**2)
print(f'O IMC dessa pessoa é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal, cuidado!')
elif 18.5 < imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 < imc < 30:
    print('Você está em SOBREPESO!')
elif 30 < imc < 40:
    print('Você está em OBESIDADE, cuidado!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')