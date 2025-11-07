'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

# Conversor de Temperaturas
# Autor: (Seu nome)
# Descrição: Converte temperaturas entre Celsius, Fahrenheit e Kelvin.

def converter_temperatura(valor, origem, destino):
    origem = origem.lower()
    destino = destino.lower()

    # Primeiro, converte tudo para Celsius
    if origem == "celsius":
        celsius = valor
    elif origem == "fahrenheit":
        celsius = (valor - 32) * 5 / 9
    elif origem == "kelvin":
        celsius = valor - 273.15
    else:
        raise ValueError("Unidade de origem inválida!")

    # Depois, converte de Celsius para a unidade desejada
    if destino == "celsius":
        return celsius
    elif destino == "fahrenheit":
        return (celsius * 9 / 5) + 32
    elif destino == "kelvin":
        return celsius + 273.15
    else:
        raise ValueError("Unidade de destino inválida!")


# Programa principal
print("=== Conversor de Temperatura ===")
valor = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (Celsius, Fahrenheit, Kelvin): ")
destino = input("Informe a unidade de destino (Celsius, Fahrenheit, Kelvin): ")

try:
    resultado = converter_temperatura(valor, origem, destino)
    print(f"\n{valor:.2f} {origem.capitalize()} = {resultado:.2f} {destino.capitalize()}")
except ValueError as e:
    print(f"Erro: {e}")
