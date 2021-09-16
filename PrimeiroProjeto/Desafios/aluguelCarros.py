diasAlugados=int(input('Quantos dias alugados? '))
quantosKM=int(input('Quantos KM rodados? '))
totalPagar= (diasAlugados * 60) + (quantosKM * 0.15)
print('O total a pagar é de R${:.2f} '.format(totalPagar))