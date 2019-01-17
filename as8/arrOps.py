from turtle import *;
from time import *;

# ---------------------------------------------------
# Function: drawRectangle(...)
# draw a rectangle 
# Its left corner is located at  (x, 0)
# width: 5 pixel
# height is the "height" parameter given
# fill color is the given "sColor"
# ---------------------------------------------------
def drawRectangle(x, height, sColor):
	speed(0);
	#----------------------
	# You job here 
	#------------------------
	penup()
	pencolor("white")
	goto(x,0)
	pendown()
	setheading(0)
	fillcolor(sColor)
	begin_fill()
	for i in range(4):
		if i%2==0:
			forward(5)
		else: 
			forward(height)
		left(90)
	end_fill()
# ---------------------------------------------------
# drawArrElement(...)
# Draw a bar for the i'th element of the given array
# location of the left-bottom corner: (i*10, 0)
# width of the bar: 5 pixel
# height of the bar: arr[i]
# Attention: you need to achieve a FLASHING effect below
#    You should first clear the bar (height 1000) with WHITE color
#    draw the bar in color RED
#    pause for the "pauseTime" seconds
#    draw the bar in color BLACK
# ---------------------------------------------------
def drawArrElement(arr, i, pauseTime):
	#------------------------
	# You job here
	drawRectangle(i*10,1000,"white")
	drawRectangle(i*10,arr[i],"red")
	drawRectangle(i*10,arr[i],"black")
	delay(pauseTime)
		
		
	return;

# -----------------------------------------------------
# draw an entire array by calling drawArrElement(...)
# -----------------------------------------------------
def drawArr(arr):
	#------------------------
	# You job here 
	#------------------------
	for i in range(len(arr)):
		drawArrElement(arr, i, 1)
	return;

# -----------------------------------------------------
# set the value of element located at index i of the array
# draw the write operation
# -----------------------------------------------------
def setArrElement(arr, i, val): 
	#------------------------
	# You job here 
	#------------------------
	arr[i] = val;
	drawArrElement(arr, i, 1)
	return;
