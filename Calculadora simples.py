# Calculadora simples
print('1 - adição')
print('2 - subtração')
print('3 - multiplicacão')
print('4 - divisão')
option = int(input("escolha uma operação:") )

if(option in [1, 2, 3, 4]):
    num1 = int(input('digite o primeiro numero: '))
    num2 = int(input('digite o segundo numero: '))

if(option == 1):
    result = num1 + num2

elif(option == 2):
    result = num1 - num2
elif(option == 3):
    result = num1 * num2
elif(option == 4):
    result = num1 // num2


else:
    print('operação invalida ')

print("o resultado da operação é {}".format(result))

