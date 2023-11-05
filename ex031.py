distancia = float(input('Qual será a distância em Km da viagem? '))
passagem=distancia*.50 if distancia <=200 else distancia*.45

'''if distancia <= 200:
    passagem = distancia * .50
    print(f'O preço da passagem será de R${passagem:.2f}')
else:
    passagem = distancia * .45
    print(f"O preço da passagem será de R${passagem:.2f}")'''
print(f"O preço da passagem será de R${passagem:.2f}")