import turtle

turtle.speed(8)
turtle.color("green")

def traingle_length(length_a):
    for i in range(3):
        turtle.forward(length_a)
        turtle.left(120)

counter = 0

while counter < 35:
    traingle_length(200)
    turtle.right(10)
    counter += 1


turtle.exitonclick()
