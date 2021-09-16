frase='Machine Learning on Python'
buscar='Machine' in frase

print('>>>> {}'.format(frase[9:12]))

print('Tamanho: {} caracteres'.format(len(frase)))

print("Na posição {} encontra-se a palavra 'Python' ".format(frase.find('Python')))

print('Existe a palavra "Machine" na frase? {}.'.format(buscar))
