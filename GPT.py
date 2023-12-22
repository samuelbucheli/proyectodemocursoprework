import turtle

# Configurar la ventana
turtle.speed(2)
turtle.bgcolor("blue")

# Función para dibujar un círculo
def dibujar_circulo(color, radio, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radio)
    turtle.end_fill()

# Función para dibujar un rectángulo
def dibujar_rectangulo(color, ancho, alto, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(ancho)
        turtle.right(90)
        turtle.forward(alto)
        turtle.right(90)
    turtle.end_fill()

# Dibujar la cabeza
dibujar_circulo("yellow", 50, 0, 200)

# Dibujar el cuerpo
dibujar_rectangulo("blue", 100, 150, -50, 50)

# Dibujar los brazos
dibujar_rectangulo("blue", 20, 100, -50, 50)
dibujar_rectangulo("blue", 20, 100, 30, 50)

# Dibujar las piernas
dibujar_rectangulo("red", 20, 100, -30, -100)
dibujar_rectangulo("red", 20, 100, 10, -100)

# Ocultar la tortuga y mostrar la ventana
turtle.hideturtle()
turtle.done()
