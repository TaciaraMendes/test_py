'''1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada'''


# Função para calcular a gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Programa principal
print("=== Calculadora de Gorjeta ===")

# Pede os valores para o usuário
valor_conta = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

# Chama a função e guarda o resultado
valor_da_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

# Mostra o resultado
print("O valor da gorjeta é:", valor_da_gorjeta)
