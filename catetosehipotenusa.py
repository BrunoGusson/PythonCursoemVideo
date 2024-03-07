co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co ** 2 + ca **2)**(1/2)
print('A hipotenusa de {} e de {} corresponde a {:.2f}'.format(co, ca, hi))

