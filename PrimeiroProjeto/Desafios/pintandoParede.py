largura=float(input('Largura da parede: '))
altura=float(input('Altura da parede: '))
dimensao=('{}x{}'.format(largura,altura))
area=(largura * altura)
litrosTinta= area / (2 * 1 )
print('Sua parede tem a dimensão de {} e sua área é de {}m².\nPara pintar essa parede, você precisará de {}l de tinta.'.format(dimensao,area,litrosTinta))