from turtle import Turtle
import random

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_postion = [-100, -50, 0, 50, 100, 150]


class TurtleBet:
    def __init__(self, all_turtle):
        self.all_turtle = all_turtle
        self.winner = " "

    def create_turtle(self):
        for c in range(0, 6):
            turtle = Turtle(shape="turtle")
            turtle.color(colours[c])
            turtle.penup()
            turtle.goto(x=-230, y=y_postion[c])
            self.all_turtle.append(turtle)

        line = Turtle()
        line.penup()
        line.goto(x=250, y=200)
        line.pendown()
        line.goto(x=250, y=-200)

    def not_over(self):
        for turtle in self.all_turtle:
            if turtle.xcor() >= 250 + 10:
                return True
            else:
                return False

    def move_turtle(self):
        for turtle in self.all_turtle:
            random_forward_step = random.randint(0, 10)
            turtle.forward(random_forward_step)
            if self.not_over():
                self.winner = turtle.color()
                break
