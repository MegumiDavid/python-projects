import turtle as t
import random

directions = [0,90,180,270]

def random_color():
  colours_list = []
  for c in range(0,255+1):
    colours_list.append(c)
  colour_rgb = [random.choice(colours_list),random.choice(colours_list),random.choice(colours_list)]
  tub = (colour_rgb[0],colour_rgb[1],colour_rgb[2])
  return tub

tim = t.Turtle()
tim.speed(0)
t.colormode(255)
for c in range(0,200):
  tim.pensize(15)
  tup = random_color()
  tim.pencolor(tup)
  tim.forward(100)
  tim.setheading(random.choice(directions))

########### Challenge 4 - Random Walk ########
