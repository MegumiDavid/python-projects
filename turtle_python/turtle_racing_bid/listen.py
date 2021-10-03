from turtle import Turtle, Screen
import random

colours = ['red','orange','yellow','green','blue','purple']
y_postion = [-100,-50,0,50,100,150]

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?")


all_turtle = []
for c in range(0,6):
    turtle = Turtle(shape="turtle")

    turtle.color(colours[c])
    turtle.penup()
    turtle.goto(x=-230,y=y_postion[c])
    all_turtle.append(turtle)

line = Turtle()
line.penup()
line.goto(x=250,y=200)
line.pendown()
line.goto(x=250,y=-200)


is_over = False
while not is_over:
    for turtle in all_turtle:
        random_forward_step = random.randint(0,10)
        turtle.forward(random_forward_step)
        if turtle.position()[0] >= 250+10:
            winner = turtle.color()
            is_over = True

print(f"The winner is {winner[0]}")
if winner[0] == user_bet.lower():
    print("YOU WIN")
else:
    print("YOU LOSE")
screen.exitonclick()





