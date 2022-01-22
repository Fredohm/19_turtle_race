# Turtle Race Game
import turtle
from turtle import Turtle, Screen
from random import choice

turtle_list = []
turtle_speed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
turtle_colors = ["RoyalBlue", "Green", "Crimson", "Yellow", "Fuchsia", "OrangeRed", "DarkTurquoise"]


def set_turtle_start(p_turtle, turtle_color, y_pos):
    p_turtle.hideturtle()
    p_turtle.color(turtle_color)
    p_turtle.penup()
    p_turtle.goto(x=-240, y=y_pos)
    p_turtle.showturtle()


screen = Screen()
screen.setup(width=500, height=400)

user_bet = turtle.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

start_y_pos = -120
for turtle_index in range(0, 7):
    turtle = Turtle(shape="turtle")
    set_turtle_start(turtle, turtle_colors[turtle_index], start_y_pos)
    start_y_pos += 40
    turtle_list.append(turtle)

is_race_on = True
while is_race_on:
    for turtle_index in range(0, 7):
        # TODO fix random speed for each turtle
        turtle_list[turtle_index].speed(choice(turtle_speed))
        print(turtle_list[turtle_index].speed(choice(turtle_speed)))
        turtle_list[turtle_index].forward(5)
        x_pos = turtle_list[turtle_index].xcor()

        if x_pos > 235:
            is_race_on = False


screen.exitonclick()
