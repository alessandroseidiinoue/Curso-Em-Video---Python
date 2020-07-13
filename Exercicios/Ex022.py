nome = input('Digite o nome completo: ')
letras = nome.split()[0]
print('O nome com todas as letras maiusculas é: {}'.format(nome.upper()))
print('O nome com todas as letras minusculas é: {}'.format(nome.lower()))
print('O nome, {}, tem um total de {} letras'.format(letras, len(letras)))
