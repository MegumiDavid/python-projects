from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("light salmon")

#turtle.dot(size=5)

#for c in range (50):
#  turtle.pendown()
#  turtle.forward(10)
#  turtle.penup()
#  turtle.forward(10)

#def the_beauty_of_simetric()

pen_color = ['dark orange','firebrick','medium violet red','forest green', 'medium sea green','cornflower blue','yellow','salmon','red']

i = 0
for c in range (3,11):


  color = pen_color[i]
  for i in range (c):
    turtle.pencolor(color)
    turtle.forward(100)
    turtle.right(360/c)
  i+=1

'''
for c in range(4):
  turtle.forward(100)
  turtle.right(90)

for c in range(5):
  turtle.forward(100)
  turtle.right(72)

for c in range(6):
  turtle.forward(100)
  turtle.right(60)

for c in range(7):
  turtle.forward(100)
  turtle.right(51.4285714286)

for c in range(8):
  turtle.forward(100)
  turtle.right(45)
'''


'''
jimmy_the_turtle.forward(100)
jimmy_the_turtle.right(90)
jimmy_the_turtle.forward(100)
jimmy_the_turtle.right(90)
jimmy_the_turtle.forward(100)
'''







screen = Screen()
screen.exitonclick