# Ejercicio 3: Clasificador de Números

def clasificar_numeros(lista):
    pares = []
    impares = []
    negativos = []
    for n in lista:
        if n < 0:
            negativos.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares, negativos

# Ejemplo
nums = [10, -3, 5, -8, 12, 7, -1]
pares, impares, negativos = clasificar_numeros(nums)
print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)
