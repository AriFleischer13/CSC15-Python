from turtle import *;

# draw a rectangle.
# x, y: the coordinates of the CENTER of the rectangle
# penColor, fillColor: strings like "#FF0000"
# width, height: in pixels
def drawRectangle(x, y, penColor, fillColor, width, height):
	# -----------------------------------
	# Your job here (challenge 3)
	# -----------------------------------
	speed(50);
	penup();
	goto(x,y);
	pendown();

	setheading(0);
	fillcolor(fillColor);
	begin_fill();
	for i in range(4):
		forward(height);
		left(90);
	end_fill()

		
	
