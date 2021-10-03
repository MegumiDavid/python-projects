###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
'''
import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    color_in_rgb = color.rgb
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    new_color = (red,green,blue)
    rgb_colors.append(new_color)
'''

import turtle as t
import random
t.colormode(255)
colors_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle = t.Turtle()

'''
turtle.setheading(255)
turtle.forward(300)
turtle.setheading(0)'''
turtle.penup()
turtle.hideturtle()
turtle.setheading(270)
turtle.forward(300)
turtle.setheading(0)
turtle.speed("fastest")
number_of_dots = 100


for dot_count in range(1,number_of_dots+1):
    random_color = random.choice(colors_list)
    turtle.dot(20,random_color)
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
#print(rgb_colors)

screen = t.Screen()
screen.exitonclick()


