import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración del juego
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Atrapar la Estrella")

# Colores
blanco = (255, 255, 255)
amarillo = (255, 255, 0)

# Personaje
personaje_ancho = 50
personaje_alto = 50
personaje_x = ancho // 2 - personaje_ancho // 2
personaje_y = alto - personaje_alto - 10

# Estrella
estrella_ancho = 30
estrella_alto = 30
estrella_x = random.randint(0, ancho - estrella_ancho)
estrella_y = 0
estrella_velocidad = 5

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 36)

# Función para mostrar texto en pantalla
def mostrar_texto(texto, color, x, y):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

# Ciclo principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del personaje
    teclas_pulsadas = pygame.key.get_pressed()
    if teclas_pulsadas[pygame.K_LEFT] and personaje_x > 0:
        personaje_x -= 5
    if teclas_pulsadas[pygame.K_RIGHT] and personaje_x < ancho - personaje_ancho:
        personaje_x += 5

    # Actualizar posición de la estrella
    estrella_y += estrella_velocidad

    # Verificar colisión entre el personaje y la estrella
    if (
        personaje_x < estrella_x + estrella_ancho
        and personaje_x + personaje_ancho > estrella_x
        and personaje_y < estrella_y + estrella_alto
        and personaje_y + personaje_alto > estrella_y
    ):
        estrella_x = random.randint(0, ancho - estrella_ancho)
        estrella_y = 0
        puntuacion += 1

    # Verificar si la estrella ha llegado al fondo
    if estrella_y > alto:
        estrella_x = random.randint(0, ancho - estrella_ancho)
        estrella_y = 0

    # Limpiar la pantalla
    pantalla.fill(blanco)

    # Dibujar el personaje
    pygame.draw.rect(pantalla, amarillo, [personaje_x, personaje_y, personaje_ancho, personaje_alto])

    # Dibujar la estrella
    pygame.draw.ellipse(pantalla, amarillo, [estrella_x, estrella_y, estrella_ancho, estrella_alto])

    # Mostrar la puntuación en pantalla
    mostrar_texto("Puntuación: " + str(puntuacion), amarillo, 10, 10)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad del juego
    reloj.tick(30)
