import turtle
import random

colors = ["AliceBlue", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "SpringGreen", "SteelBlue", "yellow" ]


scr = turtle.Screen()
pen = turtle.Turtle()
def kyklos():
    pen.pu()
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    pen.setpos(x, y)
    r = random.randint(10, 80)
    pen.pd()
    color = random.choice(colors)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()
def trigwno():
    pen.pu()
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    pen.setpos(x, y)
    size = random.randint(10,100)

    pen.pd()
    color = random.choice(colors)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(3):
        pen.fd(size)
        pen.right(120)
    pen.end_fill()
def trap():
    pen.pu()
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    pen.setpos(x, y)
    size = random.randint(10, 100)

    pen.pd()
    color = random.choice(colors)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(3):
        pen.fd(size)
        pen.right(60)
    pen.end_fill()

def tetr():
    pen.pu()
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    pen.setpos(x, y)
    pleura = random.randint(10, 100)
    color = random.choice(colors)
    pen.fillcolor(color)
    pen.begin_fill()
    for times in range(4):
        pen.pd()

        pen.fd(pleura)
        pen.right(90)
    pen.end_fill()
shapes = [tetr, trigwno, kyklos, trap]
for i in range(500):
    pen.speed(100)
    shapechoice = random.choice(shapes)
    shapechoice()
turtle.exitonclick()
