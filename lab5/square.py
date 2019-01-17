from turtle import *
speed(100)
c = 0
i = 0
setheading(90)
for x in range(80):
	forward(200-c)
	left(90)
	i = i + 1
	if i == 4: 
		c = c + 10
		i = 0
		goto(0,0)

input()
