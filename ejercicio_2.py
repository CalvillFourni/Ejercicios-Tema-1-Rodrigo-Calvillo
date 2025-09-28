# Ejercicio 2: Simulador de Ahorro Mensual

def simulador_ahorro(cantidad_inicial, cantidad_mensual, meses):
    total = cantidad_inicial + cantidad_mensual * meses
    if total > 5000:
        print(f"¡Felicidades! Has ahorrado {total}€")
    else:
        print(f"Total ahorrado: {total}€")
    return total

# Ejemplo
simulador_ahorro(1000, 300, 15)
