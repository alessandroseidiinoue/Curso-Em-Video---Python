nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média da nota {:.1f} e {:.1f} é {:.1f}.'.format(nota1, nota2, media))
if media >= 5 and media < 7:
    print('Aluno em RECUPERAÇÃO')
elif media < 5:
    print('Aluno REPROVADO')
else:
    print('Aluno APROVADO')