from arrOps import *;

def bubble_sort(arr):
	#-------------------------
	# your job here
	#-------------------------
	for round in range(len(arr)-1):
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				temp = arr[i];
				setArrElement(arr, i, arr[i+1])
				setArrElement(arr, i+1, temp)
				
	return;

arr1 = [100, 150, 200, 120, 300, 250, 240, 230, 130, 300, 200, 330,
	340, 240, 120, 230, 350, 110, 220, 250, 320, 270];
drawArr(arr1);
input("Enter to continue sort!");
bubble_sort(arr1);
input("Enter to complete!");
