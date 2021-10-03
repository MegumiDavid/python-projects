
from turtle import Turtle, Screen
from turtle_oop import TurtleBet
import random


screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?")


turtle_list = []
turtle_bet = TurtleBet(turtle_list)
turtle_bet.create_turtle()


is_over = False
while not turtle_bet.not_over():
    turtle_bet.move_turtle()

print(turtle_bet.winner)
'''
print(f"The winner is {winner}")
if winner[0] == user_bet.lower():
    print("YOU WIN")
else:
    print("YOU LOSE")
'''
screen.exitonclick()





