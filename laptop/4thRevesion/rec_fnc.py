import turtle

turtle.color("red")
turtle.speed(3)

def draw_rec(length_rec):
    for i in range(3):
        turtle.forward(length_rec)
        turtle.left(120)

draw_rec(300)
turtle.color("blue")

turtle.exitonclick()
