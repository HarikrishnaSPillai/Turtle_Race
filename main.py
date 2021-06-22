import random
from turtle import Turtle, Screen

is_Race = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make a bet", "Which turtle will  win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-230, start_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_Race = True

while is_Race:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_Race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won")
            else:
                print(f"You lost, {winning_color} won the race")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
