from typing import Match
catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa =  (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
