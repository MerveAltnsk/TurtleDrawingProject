import turtle

turtle_screen = turtle.Screen()                # Ekran oluşturma
turtle_screen.bgcolor("black")
turtle_screen.title("Turtle Drawing Project")

turtle_instance = turtle.Turtle()
turtle_instance.color("yellow")
turtle_instance.speed(5)
turtle_instance.shape("circle")

turtle_colars = ["yellow", "white", "red", "green", "OliveDrab", "blue", "orange", "brown", "pink",]


for i in range(20):
    turtle_instance.color(turtle_colars[ i % len(turtle_colars)])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)


turttle.mainloop()
#turtle.done()