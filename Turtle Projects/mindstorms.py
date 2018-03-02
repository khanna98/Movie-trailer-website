import turtle

class shape:
	def __init__(self):
		self.window = turtle.Screen()
		self.window.bgcolor("red")
		self.draw_square()
		self.draw_circle()
		self.draw_triangle()
		self.window.exitonclick()

	def draw_square(self):
		self.brad = turtle.Turtle()
		self.brad.speed(2)
		self.brad.shape("turtle")
		self.brad.color("yellow")
		for i in range(0,3):
			self.brad.fd(100)
			self.brad.rt(90)
		self.brad.fd(100)

	def draw_circle(self):
		self.angie = turtle.Turtle()
		self.angie.circle(100)
		self.angie.speed(50)
		self.angie.shape("arrow")
		self.angie.color("blue")
	def draw_triangle(self):
		self.ben = turtle.Turtle()
		self.ben.rt(90)
		self.ben.fd(100)
		self.ben.rt(90)
		self.ben.fd(70)
		self.ben.rt(135)
		self.ben.fd(100)
		self.ben.speed(2)
		self.ben.shape("turtle")

x = shape()
