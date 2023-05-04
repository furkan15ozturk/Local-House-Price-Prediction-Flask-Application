# import re
#
# room = "3.5 + 1"
# room_value = 0
# numbers = re.findall(r'\d+\.\d+|\d+', room)
# if len(numbers) == 2:
#     room_value = eval(numbers[0] + '+' + numbers[1])
# elif len(numbers) == 1:
#     room_value = int(numbers[0])
# else:
#     room_value = None
# print(room_value)

import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw the infinity symbol
for i in range(100):
    t.right(2)
    t.forward(2)
    t.left(4)
    t.forward(2)

# Draw the heart
t.penup()
t.goto(0, -100)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.left(45)
t.forward(100)
t.circle(50, 180)
t.right(90)
t.circle(50, 180)
t.forward(100)
t.end_fill()

# Draw the "ILY" letters
t.penup()
t.goto(0, -200)
t.pendown()
t.write("I   L   Y", align="center", font=("Arial", 24, "bold"))

# Keep the window open until it is closed manually
turtle.done()

