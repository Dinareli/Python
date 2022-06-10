turno=(input('Você estuda em qual turno? Digite M para matutino, V para vespertino ou N para noturno\n'))
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else: 
    print('Valor inválido.')