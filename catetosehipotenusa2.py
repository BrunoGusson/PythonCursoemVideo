import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(co , ca)
print('A hipotenusa de {} e de {} corresponde a {:.2f}'.format(co , ca , hi))
