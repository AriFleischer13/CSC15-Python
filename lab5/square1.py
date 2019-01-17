from turtle import *

speed(100);
size = 0;
for i in range(20):
	setheading(90)
	size = size + 10
	for x in range(4):
		forward(size)
		left(90)
input()
