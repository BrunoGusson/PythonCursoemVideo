larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg , alt, área))
tinta = área / 2
print('Para pintar a parede será preciso {} litros de tinta'.format(tinta))
