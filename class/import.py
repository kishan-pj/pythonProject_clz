
import turtle
screen=turtle.Screen()
pen=turtle.Turtle()

def drawCircle(x,y,r):
    pen.pu()
    pen.goto(x,y-r)
    pen.pd()
    pen.circle(r)


for i in range(20,200,20):
    drawCircle(0,0,i)
    pen.begin_fill()
    pen.color("red")
    pen.fillcolor("blue")

turtle.done()