# Turtle Race Game
import turtle
from turtle import Turtle, Screen


def set_turtle_start(p_turtle, turtle_color, y_pos):
    p_turtle.hideturtle()
    p_turtle.color(turtle_color)
    p_turtle.penup()
    p_turtle.goto(x=-240, y=y_pos)
    p_turtle.showturtle()


screen = Screen()
screen.setup(width=500, height=400)

user_bet = turtle.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

blue_turtle = Turtle(shape="turtle")
set_turtle_start(blue_turtle, "RoyalBlue", 120)

green_turtle = Turtle(shape="turtle")
set_turtle_start(green_turtle, "Green", 80)

red_turtle = Turtle(shape="turtle")
set_turtle_start(red_turtle, "Crimson", 40)

yellow_turtle = Turtle(shape="turtle")
set_turtle_start(yellow_turtle, "Yellow", 0)

purple_turtle = Turtle(shape="turtle")
set_turtle_start(purple_turtle, "Fuchsia", -40)

orange_turtle = Turtle(shape="turtle")
set_turtle_start(orange_turtle, "OrangeRed", -80)

turquoise_turtle = Turtle(shape="turtle")
set_turtle_start(turquoise_turtle, "DarkTurquoise", -120)

screen.exitonclick()
