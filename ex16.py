resp=(input('Você deseja passar a temperatura para Fahrenheit ou  Celsius? Digite F para Fahrenheit ou C para Celsius.\n'))

if resp == 'F':
    temp1=float(input('Digite o valor que deseja converter:\n'))
    Fah= (temp1 * 1.8) + 32
    print("O valor é ",Fah)
elif resp == 'C':
    temp2=float(input('Digite o valor que deseja converter:\n'))
    cel=(temp2 - 32) / 1.8
    print("O resultado é ",cel)