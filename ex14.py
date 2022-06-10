p=(input('Você têm irmãos?\n'))
s='sim'
n='não'

if p == s:
    print('Quantos irmãos você tem?')
    resp1=(input())
elif p == n:
    print('Gostaria de ter?')
    resp2=(input())
    if resp2 == s:
        print('Quantos?')
        resp3=int(input())
    elif resp2 == n:
        print('Compreensível haha')