import turtle

screen = turtle.Screen()                # Ekran oluşturma
screen.bgcolor("DarkGreen")
screen.title("Turtle Drawing Project")

'''
turtle_instance = turtle.Turtle()       # Başlangıç
turtle_instance2 = turtle.Turtle()


turtle_instance.pencolor("yellow")
turtle_instance.speed(5)
turtle_instance.shape("turtle")
turtle_instance.forward(200)            # 100 piksel ileri git


turtle_instance2.pencolor("red")
turtle_instance.speed(5)
turtle_instance2.shape("turtle")
turtle_instance2.left(90)
turtle_instance2.forward(200)
'''

'''
### square

turtle3 = turtle.Turtle()
turtle3.pencolor("chartreuse2")
turtle3.speed(5)
turtle3.shape("turtle")

for i in range(4):
    turtle3.forward(100)
    turtle3.left(90)
    turtle3.forward(100)

turtle3.left(90)
'''
'''
### star

turtle4 = turtle.Turtle()
turtle4.pencolor("yellow")
turtle4.speed(10)
turtle4.shape("turtle")

for i in range(5):
    turtle4.left(144)
    turtle4.forward(200)
'''

### polygon

turtle5 = turtle.Turtle()
turtle5.pencolor("yellow")
turtle5.speed(10)
turtle5.shape("turtle")

num_sides = 8
angle = 360 / num_sides
side_length = 100

for i in range(num_sides):
    turtle5.left(angle)
    turtle5.forward(side_length)

turtle.done()                           # Ekran kapanmaması için bunu yazıyoruz
