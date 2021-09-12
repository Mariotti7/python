distancia=float(input("Uma distância em metros: "))
quilometros= distancia * 0.001
hectometros= distancia * 0.01
decametros= distancia * 0.1
decimetros= distancia * 10
centimetros = distancia * 100
milimetros = distancia * 1000
print("A medida de {}m corresponde a ".format(distancia))
print("{}km".format(quilometros))
print("{}hm".format(hectometros))
print("{}dam".format(round(decametros,1)))
print("{}dm".format(int(decimetros)))
print("{}cm".format(int(centimetros)))
print("{}mm".format(int(milimetros)))
