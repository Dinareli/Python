n1=int(input('Digite um número\n'))
n2=int(input('Digite outro número\n'))
mult = n1 * n2
div = n1 / n2
resp=(input('O que deseja fazer agora? multiplicar ou dividir? Digite M para multiplicar ou D para dividir.\n'))

if resp == 'M':
    (print('O resultado é ' ,mult))
elif resp == 'D':
    (print('O resultado é' ,div))
else:
    print('Resposta inválida.')