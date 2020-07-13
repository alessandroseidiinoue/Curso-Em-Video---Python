salario = float(input('Digite o seu salário: \033[30mR$ \033[m'))
if salario > 1250:
    novo = salario + (salario * 0.10)
else:
    novo = salario + (salario * 0.15)
print('O novo salário será de R$ {:.2f}'.format(novo))
