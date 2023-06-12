from turtle import Turtle, Screen
import random

new_turtle = Turtle()
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")
colours = ["red", "orange", "yellow", "green", "SkyBlue", "CadetBlue", "purple"]
y_positions = [-90, -60, -30, 0, 30, 60, 90, 120]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won!🎉 {winning_turtle} turtle is the winner!")
            else:
                print(f"You lose😬, {winning_turtle} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
