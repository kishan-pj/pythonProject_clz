
# import turtle
from turtle import *
screen =Screen()
pen=Turtle()
pen.speed(7)
pen.shape("circle")
pen.width(5)
pen.color("green")
pen.fillcolor("red")

pen.begin_fill()
for i in range(4):
    pen.forward(200)
    pen.right(90)
    pen.fillcolor("blue")
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.fillcolor()
    pen.forward(200)
    pen.end_fill()
# done
screen.exitonclick()
