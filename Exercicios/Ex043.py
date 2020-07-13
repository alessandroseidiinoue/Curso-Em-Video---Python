peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do Peso')
elif 25 > imc >= 18.5:
    print('Peso Ideal')
elif 30 > imc >= 25:
    print('Sobrepeso')
elif 40 > imc >= 30:
    print('Obesidade')
else:
    print('Obesidade Morbita')
print(imc)
