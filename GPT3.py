import turtle
from turtle import RawTurtle, ScrolledCanvas
from PIL import ImageGrab

# Configurar la ventana
turtle.speed(0)
turtle.bgcolor("white")

# Función para dibujar un círculo
def dibujar_circulo(color, radio, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radio)
    turtle.end_fill()

# Función para dibujar un mandala simple
def dibujar_mandala():
    for _ in range(36):
        turtle.color("blue")
        turtle.circle(100)
        turtle.right(10)

# Dibujar el mandala
dibujar_mandala()

# Guardar el mandala como una imagen
# (Nota: Esto solo funciona en entornos de escritorio, no en entornos en línea)
canvas = turtle.getcanvas()
x, y, w, h = canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_width(), canvas.winfo_height()
ImageGrab.grab(bbox=(x, y, x + w, y + h)).save("mandala.png")

# Mantener la ventana abierta
turtle.mainloop()
