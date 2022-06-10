preco1=int(input('Diga o preço do produto que deseja comprar:\n'))
preco2=int(input('Diga um segundo valor do mesmo produto:\n'))
preco3=int(input('Diga mais um preço do mesmo produto\n'))

if preco1 < preco2 and preco1 < preco3:
    print('Você deve levar o produto com o valor de ' ,preco1, ' reais')
elif preco2 < preco1 and preco2 < preco3:
    print('Você deve levar o produto com o valor de ' ,preco2, ' reais')
else:
    print('Você deve levar o produto com o valor de ' ,preco3, ' reais')
