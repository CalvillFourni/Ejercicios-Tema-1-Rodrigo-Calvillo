# Ejercicio 6: Inventario de Personajes

def inventario(personajes):
    humanos = sorted([p for p, tipo in personajes.items() if tipo == "humano"])
    criaturas = sorted([p for p, tipo in personajes.items() if tipo == "criatura"], key=len)
    return humanos, criaturas

# Ejemplo
personajes = {
    "Aragorn": "humano",
    "Legolas": "criatura",
    "Frodo": "humano",
    "Smaug": "criatura",
    "Gandalf": "humano"
}

humanos, criaturas = inventario(personajes)
print("Humanos:", humanos)
print("Criaturas:", criaturas)
