import pygame 
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración del juego
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Adivina el Número")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Generar un número aleatorio
numero_secreto = random.randint(1, 20)

# Función para mostrar texto en la pantalla
def mostrar_texto(texto, fuente, color, x, y):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

# Ciclo principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    pantalla.fill(blanco)

    # Obtener la entrada del jugador
    teclas_pulsadas = pygame.key.get_pressed()
    if teclas_pulsadas[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # Adivina el número
    if teclas_pulsadas[pygame.K_RETURN]:
        intento = int(input("Adivina el número (entre 1 y 20): "))
        if intento == numero_secreto:
            print("¡Correcto! ¡Has adivinado el número!")
            pygame.quit()
            sys.exit()
        else:
            print("Incorrecto. ¡Inténtalo de nuevo!")

    # Mostrar instrucciones en pantalla
    fuente = pygame.font.Font(None, 36)
    mostrar_texto("Adivina el número (entre 1 y 20)", fuente, negro, 200, 250)
    mostrar_texto("Presiona Enter para adivinar", fuente, negro, 250, 300)

    # Actualizar la pantalla
    pygame.display.flip()
