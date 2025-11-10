'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.'''

# Função para calcular o preço final com desconto
def calcular_preco_final(preco, desconto_percentual):
    # Calcula o valor do desconto
    valor_do_desconto = preco * (desconto_percentual / 100)
    
    # Calcula o novo preço com o desconto aplicado
    preco_final = preco - valor_do_desconto
    
    # Arredonda o resultado para 2 casas decimais (centavos)
    preco_final = round(preco_final, 2)
    
    # Retorna o preço final
    return preco_final

# Programa principal
print("=== Calculadora de Desconto ===")

# Pede os valores ao usuário
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o desconto (%): "))

# Chama a função e guarda o resultado
preco_com_desconto = calcular_preco_final(preco, desconto)

# Mostra o resultado formatado
print("O preço final do produto com desconto é: R$", preco_com_desconto)

