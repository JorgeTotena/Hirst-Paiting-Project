#Add a new color with tkinter turtle color format to the list and to be able to use it later
# code to extract colors from an image
"""import colorgram
rgb_colors = []
colors = colorgram.extract("R.jpeg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

    """

"""REQUIREMENTS FOR THE PROJECT:
-It should have 10 x 10 rows
-Each of the dots should be 20 in size and spaced apart by around 50
-Figure out how to move the turtle


"""
import random
from turtle import Turtle, Screen
tim = Turtle()
tim.screen.colormode(255)
tim.shape("turtle")
tim.color("brown", "green")
colors = [(242, 243, 245), (231, 229, 225), (236, 243, 240), (243, 237, 242), (199, 159, 114), (69, 91, 129), (148, 85, 52), (218, 210, 115), (136, 160, 193), (27, 32, 47), (179, 161, 35), (58, 33, 22), (184, 145, 164), (123, 70, 93), (137, 175, 153), (76, 115, 78), (143, 25, 15), (61, 30, 41), (187, 97, 82), (120, 28, 43), (46, 59, 94), (99, 118, 172), (178, 96, 114), (33, 51, 44), (99, 159, 85), (66, 84, 23), (215, 174, 192), (217, 181, 172), (218, 206, 7), (159, 210, 191)]
tim.penup()
tim.hideturtle()
tim.speed(0)
x = -360
y = -280
tim.teleport(x,y)

def draw_row():
    for i in range(10):
        random_color = random.choice(colors)
        tim.dot(20, random_color )
        tim.forward(80)

def change_line(x, y):
    tim.teleport(x, y)

def draw_hirst_painting(x, y):
    for row in range(10):
        draw_row()
        y = y + 65
        change_line(x, y)






draw_hirst_painting(x, y)


print(x, y)


screen = Screen()
screen.exitonclick()