import turtle

tut = turtle.Turtle()

tut.speed(100)
def square(len,angle):
    tut.fd(len)
    tut.rt(angle)

while True:
    square(100,100)

