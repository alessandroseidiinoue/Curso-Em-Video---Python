from random import randint
from time import sleep
print('JOGO DO ACERTO!')
n = int(input('Digite o seu número entre 0 e 5, escolhido: '))
print('PROCESSSANDO...\n')
sleep(2)
c = randint(0, 5)
if n == c:
    print('Parabéns, você venceu!!!, o número sorteado foi {}'.format(c))
else:
    print('Você errou!, o número sorteadro foi {}'.format(c))
