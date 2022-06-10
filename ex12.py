perguntas = ['Telefonou para a vítima?',
'Esteve no local do crime?',
'Mora perto da vítima?',
'Devia para a vítima?',
'Já trabalhou com a vítima?']


pontos = 0

for pergunta in perguntas:
    print(pergunta)
    resposta = input('Responda sim ou não:\n').lower().replace('ã' , 'a')
    if resposta == 'sim':
        pontos = pontos+1
    elif resposta == 'não':
        pontos == pontos+0
    
if pontos == 2:
    print('Suspeito.')
elif pontos == 3 or pontos == 4:
    print('Cúmplice.')
elif pontos == 5:
    print('Assassino.')
else :
    print('Inocente')

    