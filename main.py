# Turtle Race Game
import turtle
from turtle import Turtle, Screen
from random import randint


def set_turtle_start(p_turtle, turtle_color, y_pos):
    p_turtle.hideturtle()
    p_turtle.color(turtle_color)
    p_turtle.penup()
    p_turtle.goto(x=-240, y=y_pos)
    p_turtle.showturtle()


def race():
    start_y_pos = -120
    for turtle_index in range(0, 7):
        racing_turtle = Turtle(shape="turtle")
        set_turtle_start(racing_turtle, turtle_colors[turtle_index], start_y_pos)
        start_y_pos += 40
        turtle_list.append(racing_turtle)

    is_race_on = True
    while is_race_on:
        for colored_turtle in turtle_list:
            colored_turtle.forward(randint(1, 10))

            if colored_turtle.xcor() > 230:
                is_race_on = False
                winner_color = colored_turtle.pencolor()
                if user_bet.lower() == winner_color.lower():
                    print(f"You've won! The {winner_color.lower()} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner_color.lower()} turtle is the winner!")


screen = Screen()
screen.setup(width=500, height=400)

turtle_list = []
turtle_colors = ["Blue", "Green", "Red", "Yellow", "Violet", "Orange", "Turquoise"]

user_bet = turtle.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
race()
screen.exitonclick()
