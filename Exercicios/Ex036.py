casa = float(input('Valor da Casa: R$ '))
salario = float(input('Salário do Comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestação))
minimo = salario * 30 / 100
if prestação <= minimo:
    print('APROVADO')
else:
    print('NEGADO')