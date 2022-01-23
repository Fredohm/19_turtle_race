# Turtle Race Game
import turtle
from turtle import Turtle, Screen
from random import choice


def set_turtle_start(p_turtle, turtle_color, y_pos):
    p_turtle.hideturtle()
    p_turtle.color(turtle_color)
    p_turtle.penup()
    p_turtle.goto(x=-240, y=y_pos)
    p_turtle.showturtle()


def race():
    winner_color = ""
    start_y_pos = -120
    for turtle_index in range(0, 7):
        racing_turtle = Turtle(shape="turtle")
        set_turtle_start(racing_turtle, turtle_colors[turtle_index], start_y_pos)
        start_y_pos += 40
        turtle_list.append(racing_turtle)

    is_race_on = True
    while is_race_on:
        for turtle_index in range(0, 7):
            turtle_list[turtle_index].forward(choice(turtle_move))

            if turtle_list[turtle_index].xcor() > 235:
                is_race_on = False
                winner_color = turtle_colors[turtle_index]

    if user_bet.lower() == winner_color.lower():
        print("You win!")
    else:
        print("Sorry, you loose!")


screen = Screen()
screen.setup(width=500, height=400)

turtle_list = []
turtle_move = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
turtle_colors = ["Blue", "Green", "Red", "Yellow", "Violet", "Orange", "Turquoise"]

user_bet = turtle.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
race()
screen.exitonclick()
