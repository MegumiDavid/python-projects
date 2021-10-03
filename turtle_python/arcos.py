import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
tim.speed(200)
for c in range(0,37):
  #random_color = random_color()
  tim.pencolor(random_color())
  tim.circle(100)
  tim.right(10)


