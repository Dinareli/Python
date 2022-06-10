num1=int(input('Diga um número:\n'))
num2=int(input('Diga outro número\n'))
num3=int(input('Diga mais um número\n'))

if num1 > num2 and num1 > num3:
    print(num1, ' é maior que ' ,num2, ' e ' ,num3)
elif num2 > num1 and num2 > num3:
    print(num2, ' é ,aior que ' ,num1, ' e ' ,num3)
else:
    print(num3, ' é maior que ' ,num1, ' e ' ,num2)