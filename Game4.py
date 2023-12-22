import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración del juego
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego Didáctico")

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)

# Puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 36)

# Lista de objetos
objetos = []

# Función para mostrar texto en pantalla
def mostrar_texto(texto, color, x, y):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

# Función para crear un nuevo objeto
def crear_objeto():
    tipo = random.choice(["azul", "rojo"])
    x = random.randint(50, ancho - 50)
    y = random.randint(50, alto - 50)
    objetos.append({"tipo": tipo, "x": x, "y": y})

# Ciclo principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            for objeto in objetos:
                if (
                    objeto["tipo"] == "azul"
                    and objeto["x"] - 25 < x < objeto["x"] + 25
                    and objeto["y"] - 25 < y < objeto["y"] + 25
                ):
                    puntuacion += 1
                    objetos.remove(objeto)
                elif (
                    objeto["tipo"] == "rojo"
                    and objeto["x"] - 25 < x < objeto["x"] + 25
                    and objeto["y"] - 25 < y < objeto["y"] + 25
                ):
                    puntuacion -= 1
                    objetos.remove(objeto)

    # Crear nuevos objetos de forma aleatoria
    if random.randint(0, 100) < 5:
        crear_objeto()

    # Limpiar la pantalla
    pantalla.fill(blanco)

    # Dibujar los objetos
    for objeto in objetos:
        if objeto["tipo"] == "azul":
            pygame.draw.circle(pantalla, azul, (objeto["x"], objeto["y"]), 25)
        elif objeto["tipo"] == "rojo":
            pygame.draw.circle(pantalla, rojo, (objeto["x"], objeto["y"]), 25)

    # Mostrar la puntuación en pantalla
    mostrar_texto("Puntuación: " + str(puntuacion), azul, 10, 10)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad del juego
    pygame.time.delay(100)
