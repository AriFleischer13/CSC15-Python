from turtle import *

setheading(90);
speed(100);
size = 10
x = 0
y =0
for i in range(10):
	penup()
	goto(x,y)
	pendown()
	forward(size)
	size = size + 10
	x = x + 5
hideturtle()	
input()	
