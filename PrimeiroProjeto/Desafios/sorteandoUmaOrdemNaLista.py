import random
primeiro=input('Primeiro aluno: ')
segundo=input('Segundo aluno: ')
terceiro=input('Terceiro aluno: ')
quarto=input('Quarto aluno: ')
quinto=input('Quinto aluno: ')

sorteio= [primeiro, segundo, terceiro, quarto, quinto]
escolhido=random.shuffle(sorteio)

ordem=random.sample(sorteio, len(sorteio))
print('A ordem de apresentação será\n {}'.format(ordem))