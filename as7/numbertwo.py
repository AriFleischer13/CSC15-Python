from turtle import *;

# draw a bar chart of given array
# the width of each bar should be 5 pixels
# the space between each two bars should be 2 pixels
# the height of each bar is the VALUE of the element in the array:x
def drawBar(x,width, height):
	speed = 500
	penup()
	goto(x,0)
	pendown()
	fillcolor("black")
	begin_fill();
	setheading(0)
	for x in range(4):
		if x%2==0:
			forward(width);
			left(90)
		if x%2!=0:
			forward(height);
			left(90);
	end_fill()
	
def drawBarChart(arr):
	x2 = 0
	for z in arr:
		drawBar(x2,5,z)
		x2 = x2 + 7
	return;
