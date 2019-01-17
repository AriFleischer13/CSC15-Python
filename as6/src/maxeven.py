maxeven = 0
for i in range(arr):
	if i%2==0 and i>maxeven:
		maxeven = i
print(maxeven)
