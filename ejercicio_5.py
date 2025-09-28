# Ejercicio 5: Generador de ADN
import random

def generar_adn(n):
    letras = ['A', 'T', 'C', 'G']
    cadena = ''.join(random.choice(letras) for _ in range(n))
    conteo = {letra: cadena.count(letra) for letra in letras}
    return cadena, conteo

# Ejemplo
adn, conteo = generar_adn(20)
print("Cadena ADN:", adn)
print("Conteo:", conteo)
