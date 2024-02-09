dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O total há pagar é {:.2f}'.format(pago))
