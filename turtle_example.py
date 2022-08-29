import turtle


# forward()
# backward()
# right()
# left()
# penup()
# pendown()
# color()
# fillcolor()
# heading()
# position()
# goto()
# begin_fill()
# end_fill()
# dot()
# circle()
# home()






# Square
# skk = turtle.Turtle()
# for i in range(4):
# 	skk.forward(50)
# 	skk.right(90)
	
# turtle.done()



# Star


# star = turtle.Turtle()

# star.right(75)
# star.forward(100)

# for i in range(4):
# 	star.left(144)
# 	star.forward(100)
	
# turtle.done()




# Hexagon


# polygon = turtle.Turtle()

# num_sides = 10
# side_length = 70
# angle = 360.0 / num_sides

# for i in range(num_sides):
# 	polygon.forward(side_length)
# 	polygon.right(angle)
	
# turtle.done()






# Helix

polygon = turtle.Turtle()

turtle.speed(2)

for i in range(100):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)

turtle.done()





