import turtle

# Creamos la ventana del juego
wn = turtle.Screen()
wn.title("Ping-Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Marcador
marcadorA = 0
marcadorB = 0

# Creamos en pantalla Jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

# Creamos en pantalla Jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

# Creamos en pantalla Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

# Modificar estas variables para cambiar velocidad de la pelota
pelota.dx = 0.5
pelota.dy = 0.5

# Pen para dibujar el marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador A:0         Jugador B:0", align="center",font=("Courier", 25, "normal"))

# Linea divisoria
division = turtle.Turtle()
division.color("red")
division.goto(0,400)
division.goto(0,-400)

# Funciones de movimientos
def jugadorA_up():
    y = jugadorA.ycor()
    y += 50
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 50
    jugadorA.sety(y)

def jugadorB_up():
    y = jugadorB.ycor()
    y += 50
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 50
    jugadorB.sety(y)

# Teclado
wn.listen()
wn.onkeypress(jugadorA_up,"w")
wn.onkeypress(jugadorA_down,"s")
wn.onkeypress(jugadorB_up,"Up")
wn.onkeypress(jugadorB_down,"Down")



while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Revisa coliciones con los bordes de la ventana
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    # Si la pelota sale por la izquierda o derecha, esta regresa al centro
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()

        # Esta linea de codigo vuelve a pintar el marcador, utlizo "format" de la version 3.6 en adelante de python.
        # Si tienes python menor a la version 3.6 esta parte no te funcionara.
        pen.write(f"Jugador A: {marcadorA}      Jugador B: {marcadorB}", align="center", font=("Courier", 25, "normal") )

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()

        # Esta linea de codigo vuelve a pintar el marcador, utlizo "format" de la version 3.6 en adelante de python.
        # Si tienes python menor a la version 3.6 esta parte no te funcionara.
        pen.write(f"Jugador A: {marcadorA}      Jugador B: {marcadorB}", align="center", font=("Courier", 25, "normal"))

    # Revisa las colisiones
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
                        and (pelota.ycor() < jugadorB.ycor() + 50
                        and pelota.ycor() > jugadorB.ycor() - 50)):
            pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugadorA.ycor() + 50
                 and pelota.ycor() > jugadorA.ycor() - 50)):
        pelota.dx *= -1


