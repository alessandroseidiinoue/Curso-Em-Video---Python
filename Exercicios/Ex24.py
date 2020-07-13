cidade = str(input('Digite a cidade em que você nasceu? ')).strip()
santo = 'Santo' in cidade
print(santo)
print(cidade[:5] == 'Santo')
print(cidade[:5].upper() == 'SANTO')