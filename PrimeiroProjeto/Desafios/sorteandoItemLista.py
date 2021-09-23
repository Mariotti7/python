import random
primeiro=input('Primeiro aluno: ')
segundo=input('Segundo aluno: ')
terceiro=input('Terceiro aluno: ')
quarto=input('Quarto aluno: ')
quinto=input('Quinto aluno: ')

sorteio= [primeiro, segundo, terceiro, quarto, quinto]
escolhido=random.choice(sorteio)

ordem=random.sample(sorteio, len(sorteio))
print('O aluno escolhido foi {}'.format(ordem))