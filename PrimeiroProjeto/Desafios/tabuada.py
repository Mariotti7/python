valor=int(input('Digite um número para ver sua tabuada: '))
print('--------------')
for i in range(11):
    print("{} x {} = {}".format(valor,i,(valor*i)))
print('--------------')