numero = int (input('Digite um número de 1 a 10: '))
limite = 11
while numero < limite:
    if numero > limite:
        print('Número maior que 10')
        break
    else:
        print(str(numero))
        break
print('FIM')
