dia=int(input('Qual o dia do seu aniversário?\n'))
mes=int(input('Qual o mês do seu aniversário?\n'))
ano=int(input('Qual o ano que você nasceu?\n'))

if dia > 1 and dia < 32:
    print('')
else:
    print('Dia inexistente')

if mes > 1 and mes < 13:
    print('')
else:
    print('Mês inexistente')  

if ano > 0000 and ano < 2022:
    print('')
else:
    print('Ano inexistente')
