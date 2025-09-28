# Ejercicio 1: Decodificador de Mensajes Secretos

import re

def decodificar_mensaje(mensaje):
    
    mensaje_volteado = mensaje[::-1]
    
    
    mensaje_limpio = re.sub(r'[^a-zA-Z]', '', mensaje_volteado)
    
   
    return mensaje_limpio


texto = "rOjem le se ogirdoR!@#$"

# Ejecución
print(decodificar_mensaje(texto)) 
