import turtle
turtle.Screen().bgcolor("pink")
t = turtle.Turtle()
t.penup()
t.pendown()
t.speed(100)
t.goto(0, 0)
t.color("teal")

#here iam adding the colors
colors = ["blue","Light blue","black","gray"]
for i in range(1000) :
    t.color( colors[i%4])
    t.forward (60 + i)
    t.left (40)

#here iam moving the shape
for i in range(10):
    t.forward(65)
    t.left(80)

for i in range (45) :
    t.forward (66 + 1)
    t.left (33)

#here i am ending the shape
turtle.exitonclick()