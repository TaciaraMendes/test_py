# Classificação de números pares e ímpares




print("\n=== Classificação de Números ===")

pares = 0
impares = 0

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")

    if numero.lower() == "sair":
        break

    numero = int(numero)

    if numero % 2 == 0:
        print("O número é par.")
        pares += 1
    else:
        print("O número é ímpar.")
        impares += 1

print("\n=== Resultado Final ===")
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
