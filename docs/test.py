import turtle

# side_length = 100
# angle = 90
# for side_number in range(4):
#     turtle.forward(side_length)
#     turtle.left(angle)

# turtle.circle(50)
# print(turtle.position())


## Star with odd n
n = 5
d = 200
for i in range(n):
    angle = 180.0 - 180.0 / n
    turtle.forward(d)
    # turtle.forward(d)
    turtle.left(angle)

turtle.exitonclick()
turtle.mainloop()