from datetime import date
atual = date.today().year
anos = int(input('Digite o ano de nascimento: '))
idade = atual - anos
print('''Sexo:
[ 1 ] Masculino
[ 2 ] Feminino''')
sexo = int(input('Digite a opção do SEXO: '))
if sexo != 1:
    print('O Alistamento é obritagório somente para o Sexo Masculino.')
else:
    print('Quem nasceu no ano de {}, tem hojê {} anos.'.format(anos, idade))
    if idade == 18:
        print('Você precisa de alistar imediatamente.')
    elif idade < 18:
        print('Você ainda não tem 18 anos, ainda faltam {} anos pra o alistamento.'.format(18 - idade))
        print('Seu alistamento será no ano de {}'.format(atual + (18 - idade)))
    elif idade > 18:
        print('Você ja deveria ter se alistado a {} anos.'.format(idade - 18))
        print('Seu alistamento deveria ter ocorrido no ano de {}'.format(atual - (idade - 18)))

