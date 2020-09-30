import turtle
t = turtle.Turtle()

t.shape("turtle")

#t.colormode(255)

colores = ["green", "red"]

#t.color(0,0,1)

for i in range(24):
    t.color(colores[i%2])
    t.begin_fill()
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.end_fill()

    t.left(15)

print("Hola")
