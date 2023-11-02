largura = float(input('Insira a lagura da sua parede: '))
altura = float(input('Insira a altura da sua parede: '))
area = largura*altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área e de {area}m².')
tinta = area/2
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')