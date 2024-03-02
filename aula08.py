import emoji
import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print(emoji.emojize('A raiz quadrada de {} é igual a {} :sparkles:'.format(num, math.ceil(raiz))))
