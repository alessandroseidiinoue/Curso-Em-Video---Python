from time import sleep
print('VALOR DE VIAGEM POR KM'.center(50))
viagem = int(input('Digite a distância em KM da viagem: '))
print('PROCESSANDO...')
sleep(2)
if viagem > 200:
    print('O valor da passagem para {} KM é de R$ {:.2f}'.format(viagem, viagem * 0.45))
else:
    print('O valor da passagem para {} KM é de R$ {:.2f}'.format(viagem, viagem * 0.50))
