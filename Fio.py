import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración del juego
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de Recolectar Flores")

# Colores
verde = (0, 255, 0)
azul_cielo = (135, 206, 250)
blanco = (255, 255, 255)

# Jugadora
jugadora_ancho = 50
jugadora_alto = 50
jugadora_x = ancho // 2 - jugadora_ancho // 2
jugadora_y = alto - jugadora_alto - 10
jugadora_velocidad = 5

# Flores
flores = []

# Nubes
nubes = []

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 36)

# Función para mostrar texto en pantalla
def mostrar_texto(texto, color, x, y):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

# Función para crear una nueva flor
def crear_flor():
    x = random.randint(50, ancho - 50)
    y = random.randint(50, alto - 50)
    flores.append({"x": x, "y": y})

# Función para crear una nueva nube
def crear_nube():
    x = random.randint(0, ancho - 50)
    y = random.randint(0, alto // 2)
    nubes.append({"x": x, "y": y})

# Ciclo principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de la jugadora
    teclas_pulsadas = pygame.key.get_pressed()
    if teclas_pulsadas[pygame.K_LEFT] and jugadora_x > 0:
        jugadora_x -= jugadora_velocidad
    if teclas_pulsadas[pygame.K_RIGHT] and jugadora_x < ancho - jugadora_ancho:
        jugadora_x += jugadora_velocidad

    # Actualizar posición de las flores
    for flor in flores:
        flor["y"] += 5

        # Verificar colisión entre la jugadora y la flor
        if (
            jugadora_x < flor["x"] + 30
            and jugadora_x + jugadora_ancho > flor["x"]
            and jugadora_y < flor["y"] + 30
            and jugadora_y + jugadora_alto > flor["y"]
        ):
            flores.remove(flor)
            puntuacion += 1

        # Verificar si la flor ha llegado al fondo
        if flor["y"] > alto:
            flores.remove(flor)

    # Actualizar posición de las nubes
    for nube in nubes:
        nube["y"] += 2

        # Verificar colisión entre la jugadora y la nube
        if (
            jugadora_x < nube["x"] + 50
            and jugadora_x + jugadora_ancho > nube["x"]
            and jugadora_y < nube["y"] + 30
            and jugadora_y + jugadora_alto > nube["y"]
        ):
            puntuacion -= 1
            nubes.remove(nube)

        # Verificar si la nube ha llegado al fondo
        if nube["y"] > alto:
            nubes.remove(nube)

    # Crear nuevas flores de forma aleatoria
    if random.randint(0, 100) < 5:
        crear_flor()

    # Crear nuevas nubes de forma aleatoria
    if random.randint(0, 100) < 1:
        crear_nube()

    # Limpiar la pantalla
    pantalla.fill(azul_cielo)

    # Dibujar la jugadora
    pygame.draw.rect(pantalla, verde, [jugadora_x, jugadora_y, jugadora_ancho, jugadora_alto])

    # Dibujar las flores
    for flor in flores:
        pygame.draw.circle(pantalla, blanco, (flor["x"], flor["y"]), 15)

    # Dibujar las nubes
    for nube in nubes:
        pygame.draw.circle(pantalla, blanco, (nube["x"], nube["y"]), 30)

    # Mostrar la puntuación en pantalla
    mostrar_texto("Puntuación: " + str(puntuacion), blanco, 10, 10)

    # Actual
