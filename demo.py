import turtle
def picture(x1,y1,x,y):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    for i in range(5):
        turtle.forward(x)
        turtle.left(y)
    turtle.end_fill()
turtle.speed(3)

turtle.bgcolor("red")
turtle.color("yellow")
picture(-250,230,100,144)
picture(-31,290,60,144)
picture(-30,181,60,144)
picture(-100,81,60,144)
picture(-210,65,60,144)
turtle.done()
