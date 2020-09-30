import turtle
t = turtle.Turtle()
t.shape("turtle")
colores = ["red","magenta","blue","cyan","green","yellow"]
t.left(90)
for i in range(6):
  t.color(colores[i])
  t.begin_fill()
  t.forward(100)
  t.left(120)
  t.forward(100)
  t.left(120)
  t.forward(100)
  t.left(180)
  t.end_fill()