pares = 0
impares = 0

while True:
    n = int(input("Número (0 para sair): "))
    if n == 0:
        break
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Pares:", pares)
print("Ímpares:", impares)

def classificar_numeros():
    pares = 0
    impares = 0

    while True:
        n = int(input("Número (0 para sair): "))
        if n == 0:
            break
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

p, i = classificar_numeros()
print("Pares:", p)
print("Ímpares:", i)