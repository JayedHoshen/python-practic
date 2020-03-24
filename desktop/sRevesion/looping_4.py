import turtle

turtle.shape("circle")
turtle.speed(6)

for side_length in range(5,300,10):
    for i in range(8):
        turtle.forward(side_length)
        turtle.left(90)

turtle.exitonclick()
