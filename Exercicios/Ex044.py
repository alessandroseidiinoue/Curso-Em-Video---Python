print('{:*^40}'.format(' LOJA MEGA BLASTER '))
preco = float(input('Digite o valor: '))
print('''Formas de Pagamento:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão''')
opção = int(input('Digite a opção: '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcela em 2x de R$ {:.2f}.'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    numparcela = int(input('Quantas parcelas?: '))
    parcela = total / numparcela
    print('Parcelamento com JUROS, {}x de R$ {}.'.format(numparcela, parcela))
else:
    total = preco
    print('Opção Inválida')
print('O Total de compra é de R$ {:.2f}, e o total a pagar é de R$ {:.2f}.'.format(preco, total))
