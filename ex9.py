num1 = int(input("Digite o primeiro valor:\n"))
num2 = int(input("Digite o segundo valor:\n"))
num3 = int(input("Digite o terceiro valor:\n"))
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")
