print('#'*30)
print('CALCULO DE TRIÂNGULO'.center(30))
print('#'*30)
a = float(input('Digite a \033[31mprimeira\033[m medida do triângulo: '))
b = float(input('Digite a \033[32msegunda\033[m medida do triângulo: '))
c = float(input('Digite a \033[33mterceira\033[m medida do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[7mOs valores podem formar um TRIÂNGULO!\033[m')
else:
    print('\033[41mOs valores NÃO podem formar um TRIÂNGULO!\033[m')