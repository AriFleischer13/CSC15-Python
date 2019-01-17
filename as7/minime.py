# return the sum of of an array of integers
def getSum(arr):
	iSum = 0
	for idx in arr:
		iSum += idx;
	return iSum;

# return the number of odd numbers in an array
def getCountOdd(arr):
	cOdd = 0
	for x in arr:
		if x%2!=0:
			cOdd +=1
	return cOdd;

# return the max of an array of numbers
def getMax(arr):
	max = arr[0]
	for x in range(1, len(arr)):
		if arr[x] > max:
			max = arr[x]; 
	return max;

# return the average (must be a float point number) of an array of numbers
def getAvg(arr):
	sum = 0
	for x in arr:
		sum += x;
	iAvg = sum/(len(arr));
	return iAvg;

# return a new array which is a REVERSE of the original array
def getReverse(arr):
	arr2 = []
	for x in arr:
		arr2.append(x)
	for i in range(len(arr2)//2):
		z = arr2[i]
		arr2[i] = arr2[len(arr2)-1-i];
		arr2[len(arr2)-1-i] = z
	return arr2; 

# return True if the given array is in ascending order
def isAscending(arr):
	bAscending = True
	x = arr[0];
	for idx in range(1,len(arr)):
		if x > arr[idx]:			
			bAscending = False
			break
		else:
			x = arr[idx];
		
	return bAscending;

