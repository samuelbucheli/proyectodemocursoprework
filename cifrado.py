def cifrar_mensaje(mensaje, clave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    mensaje_cifrado = ""

    for caracter in mensaje:
        if caracter.lower() in alfabeto:
            indice_original = alfabeto.index(caracter.lower())
            nuevo_indice = (indice_original + clave) % 26
            if caracter.isupper():
                mensaje_cifrado += alfabeto[nuevo_indice].upper()
            else:
                mensaje_cifrado += alfabeto[nuevo_indice]
        else:
            mensaje_cifrado += caracter

    return mensaje_cifrado

def descifrar_mensaje(mensaje_cifrado, clave):
    return cifrar_mensaje(mensaje_cifrado, -clave)

# Ejemplo de uso
mensaje_original = "Hola, ¿quieres andar conmigo?"
clave = 3

mensaje_cifrado = cifrar_mensaje(mensaje_original, clave)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave)
print("Mensaje descifrado:", mensaje_descifrado)
