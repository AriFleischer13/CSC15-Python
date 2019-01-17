from turtle import *
speed(10)
n =0
for x in range (20):
	circle(200-n)
	n = n + 10
	penup()
	goto(0,n)
	pendown()
input()
