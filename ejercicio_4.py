# Ejercicio 4: Calculadora de Notas

def calculadora_notas(notas):
    media = sum(notas) / len(notas)
    nota_max = max(notas)
    nota_min = min(notas)
    print(f"Media: {media:.2f}")
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")
    if any(n < 5 for n in notas):
        print("⚠️ Hay notas suspensas.")
    return media, nota_max, nota_min

# Ejemplo
notas = [7, 5, 9, 4, 6]
calculadora_notas(notas)
