import turtle

turtle_screen = turtle.Screen()                # Ekran oluşturma
turtle_screen.bgcolor("Light green")
turtle_screen.title("Turtle Drawing Project")

turtle_instance = turtle.Turtle()
turtle_instance.color("yellow")
turtle_instance.speed(5)
turtle_instance.shape("square")



def shrinkingSquares(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkingSquares(150)
shrinkingSquares(130)
shrinkingSquares(110)
shrinkingSquares(90)
shrinkingSquares(70)
shrinkingSquares(50)
shrinkingSquares(30)
shrinkingSquares(10)





turtle.done()