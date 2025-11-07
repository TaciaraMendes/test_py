


'''1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")
if operacao == "+":
    print(numero1 + numero2)
elif operacao == "-":
    print(numero1 - numero2)
elif operacao == "*":
    print(numero1 * numero2)
elif operacao == "/":
    print(numero1 / numero2)
else:
    print("Operação inválida!")

