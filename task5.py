import turtle

def draw_square(size, color, x, y):
    turtle.penup()
    turtle.goto(x - size/2, y - size/2)
    turtle.pendown()
    turtle.color(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.penup()
import turtle

turtle.screensize(400, 400)
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.setup(600, 600)
turtle.bgcolor("white")

size = 200
offset = size / 4
color1 = "darkgreen"
color2 = "lightgreen"
orange_size = 20

draw_square(size, color1, 0, 0)

draw_square(size, color2, offset, offset)

turtle.color("orange")
turtle.goto(offset/2, offset/2)
turtle.dot(orange_size)

turtle.done()