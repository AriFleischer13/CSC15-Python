from turtle import *;

# draw a circle given the radius
# x, y: CENTER of the circle
# radius: in pixels
def drawCircle(x, y, radius):
	# -----------------------
	# YOUR JOB HERE (challenge 2)
	# -----------------------
	speed(500)
	penup();
	goto(x,y-radius)
	pendown()
	circle(radius)
		 
