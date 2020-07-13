from time import sleep
print('-' * 50)
print('BEM VINDO AO CALCULADOR AUTOMATIZADO DE MULTA'.center(50))
print('-' * 50)
v = int(input('Digite a velocidade: '))
print('-' * 50)
print('PROCESSANDO...')
sleep(2)
print('-' * 50)
if v > 80:
    print('Você está acima da velocidade permitida.\nE será multado em R$ {:.2f}\n'.format((v - 80) * 7))
print('Tenha um Bom Dia!, Dirija com Segurança!')