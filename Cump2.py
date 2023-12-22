import time

def desear_cumpleaños(nombre):
    print(f"¡Feliz Cumpleaños, {nombre}!")
    time.sleep(1)
    print("Hoy es un día especial porque celebramos el día en que llegaste al mundo.")
    time.sleep(1)
    print(f"Te deseo un año lleno de éxitos, alegrías y momentos inolvidables, {nombre}.")
    time.sleep(1)
    print("Que cada día esté lleno de sorpresas y logros. ¡Disfruta al máximo tu día!")

# Solicitar el nombre del usuario
nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Ejecutar la función para desear feliz cumpleaños con el nombre ingresado
desear_cumpleaños(nombre_usuario)
