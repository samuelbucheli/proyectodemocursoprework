import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración del juego
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de Carros")

# Colores
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)

# Carro del jugador
carro_ancho = 50
carro_alto = 80
carro_x = ancho // 2 - carro_ancho // 2
carro_y = alto - carro_alto - 10
carro_velocidad = 5

# Obstáculos
obstaculo_ancho = 50
obstaculo_alto = 50
obstaculo_velocidad = 5
obstaculo_lista = []

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 36)

# Función para mostrar texto en pantalla
def mostrar_texto(texto, color, x, y):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

# Función para crear obstáculos
def crear_obstaculo():
    x = random.randint(0, ancho - obstaculo_ancho)
    y = -obstaculo_alto
    obstaculo_lista.append([x, y])

# Ciclo principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del carro
    teclas_pulsadas = pygame.key.get_pressed()
    if teclas_pulsadas[pygame.K_LEFT] and carro_x > 0:
        carro_x -= carro_velocidad
    if teclas_pulsadas[pygame.K_RIGHT] and carro_x < ancho - carro_ancho:
        carro_x += carro_velocidad

    # Actualizar posición de los obstáculos
    for obstaculo in obstaculo_lista:
        obstaculo[1] += obstaculo_velocidad

        # Verificar colisión entre el carro y el obstáculo
        if (
            carro_x < obstaculo[0] + obstaculo_ancho
            and carro_x + carro_ancho > obstaculo[0]
            and carro_y < obstaculo[1] + obstaculo_alto
            and carro_y + carro_alto > obstaculo[1]
        ):
            pygame.quit()
            sys.exit()

        # Verificar si el obstáculo ha llegado al fondo
        if obstaculo[1] > alto:
            obstaculo_lista.remove(obstaculo)
            puntuacion += 1

    # Crear nuevos obstáculos de forma aleatoria
    if random.randint(0, 100) < 5:
        crear_obstaculo()

    # Limpiar la pantalla
    pantalla.fill(blanco)

    # Dibujar el carro
    pygame.draw.rect(pantalla, verde, [carro_x, carro_y, carro_ancho, carro_alto])

    # Dibujar los obstáculos
    for obstaculo in obstaculo_lista:
        pygame.draw.rect(pantalla, rojo, [obstaculo[0], obstaculo[1], obstaculo_ancho, obstaculo_alto])

    # Mostrar la puntuación en pantalla
    mostrar_texto("Puntuación: " + str(puntuacion), verde, 10, 10)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad del juego
    reloj.tick(30)
