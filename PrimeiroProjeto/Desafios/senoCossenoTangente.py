import math
angulo = float(input('Digite o ângulo que você deseja: '))
sen= math.sin(math.radians(angulo))
cos= math.cos(math.radians(angulo))
tan= math.tan(math.radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sen))
print('O ângulo de {} tem o CONSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))