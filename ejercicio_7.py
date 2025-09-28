# Ejercicio 7: Analizador de URL

def analizar_url(url):
    try:
        # Separamos el protocolo del resto
        protocolo, resto = url.split("://")
        
        # Separamos el dominio y el posible recurso
        partes = resto.split("/", 1)
        dominio = partes[0]
        recurso = partes[1] if len(partes) > 1 else None

        return protocolo, dominio, recurso
    
    except Exception as e:
        return f"Error al analizar la URL: {e}"

# Ejemplos
print(analizar_url("https://www.ejemplo.com/recurso"))
print(analizar_url("http://openai.com"))
print(analizar_url("esto_no_es_una_url"))

