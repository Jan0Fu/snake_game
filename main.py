from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

segment1 = Turtle(shape="square")
segment1.color("white")
segment2 = Turtle(shape="square")
segment2.color("white")
segment2.backward(20)
segment3 = Turtle(shape="square")
segment3.color("white")
segment3.backward(40)









screen.exitonclick()
