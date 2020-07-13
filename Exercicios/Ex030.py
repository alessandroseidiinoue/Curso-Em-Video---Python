from time import sleep
print('VAMOS DESCOBRIR DE O NÚMERO É ,IMPAR, OU ,PAR,!'.center(70))
n = int(input('Digite um número qualquer: '))
print('PROCESSANDO...')
sleep(2)
if (n % 2) == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é IMPAR.'.format(n))
