import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
color_list = [(240, 238, 236), (239, 240, 246), (228, 239, 233), (213, 67, 15), (191, 173, 14), (168, 19, 37), (210, 157, 84), (55, 26, 44), (234, 209, 86), (178, 41, 65), (37, 38, 71), (135, 178, 206), (221, 74, 128), (58, 90, 161), (31, 133, 79), (51, 45, 121), (198, 132, 165), (190, 21, 14), (240, 60, 28), (74, 39, 25), (94, 189, 159), (40, 171, 192), (234, 157, 181), (243, 200, 2), (3, 116, 108), (94, 167, 76), (97, 106, 170), (228, 174, 164), (158, 209, 191)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()
