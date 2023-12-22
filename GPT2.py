import turtle

# Configurar la ventana
turtle.speed(2)
turtle.bgcolor("skyblue")

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

# Dibujar el sol
dibujar_circulo("yellow", 50, -200, 200)

# Dibujar el césped
dibujar_rectangulo("green", 800, 200, -400, -200)

# Dibujar una casa simple
dibujar_rectangulo("brown", 150, 150, -75, -50)
dibujar_rectangulo("red", 100, 100, -50, 0)

# Dibujar una puerta
dibujar_rectangulo("brown", 30, 60, -25, -50)

# Dibujar una ventana
dibujar_rectangulo("blue", 40, 40, -65, 25)

# Ocultar la tortuga y mostrar la ventana
turtle.hideturtle()
turtle.done()
