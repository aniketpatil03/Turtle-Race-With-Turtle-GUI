# -------Turtle Racing--------------#
import random
import turtle
from turtle import Turtle, Screen

game_started = False
screen = Screen()
screen.setup(height=500, width=600)     # to setup the disp window

colors_list = ["blue", "red", "green", "orange", "black", "cyan"]
y_positions = [-50, -10, 30, 70, 110, 150]

turtle_list = []

# creates 6 turtles
for turtle_index in range(0, 6):
    tutsy = Turtle(shape="turtle")
    tutsy.color(colors_list[turtle_index])
    tutsy.penup()
    tutsy.goto(x=-280, y=y_positions[turtle_index])
    turtle_list.append(tutsy)
user_guess = screen.textinput(title="Turtle Race", prompt="Which color tutsy will win the race..?")

if user_guess:
    game_started = True

while game_started:
    for tutsy in turtle_list:
        if tutsy.xcor() > 280:
            game_started = False
            if tutsy.pencolor() == user_guess:
                print(f"Winner : {tutsy.pencolor()}")
                print("wow, you won the bet...!")
            else:
                game_started = False
                print(f"Winner : {tutsy.pencolor()}")
                print("You lost!")

        # making each turtle move forward by a random disctance
        rand_move_distance = random.randint(1, 10)
        tutsy.forward(rand_move_distance)

screen.exitonclick()