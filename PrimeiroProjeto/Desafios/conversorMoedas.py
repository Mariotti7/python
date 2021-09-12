real=float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar= 5.25
conversao = real / dolar
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real,conversao))