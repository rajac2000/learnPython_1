import turtle

scr1 = turtle.Screen()
obj1 = turtle.Turtle()
#arrow, blank, circle, classic, square, triangle, turtle.
obj1.shape("blank")
obj1.pensize(1)
obj1.pencolor("Blue")

for i in range(5):
    obj1.forward(100)
    obj1.right(144)
scr1.mainloop()

