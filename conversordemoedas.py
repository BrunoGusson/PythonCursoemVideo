real = int(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/4.95
euro = real/5.37
print('Com R${:.2f} você pode comprar US$ {:.2f} e EUR${:.2F}'.format(real,dolar, euro))

