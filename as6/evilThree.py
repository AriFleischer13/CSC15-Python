from numbertwo import *;
def decoThree():
	# ---------------------------------
	# Your job here (Challenge 4)
	# ---------------------------------
	speed(500);
	iSize = 500;
	x = -300;
	y = -300;
	for i in range(50):
		penup();
		goto(x,y);
		pendown();
		if i%2==0:
			drawRectangle(x, y, "black", "black", iSize, iSize);
		else:
			drawRectangle(x, y, "black", "white", iSize, iSize);
		iSize = iSize - 10;
		x += 5;
		y += 5;
decoThree();
input();
