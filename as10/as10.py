import re;

def extractCourse():
	f1 = open("hofstra.html","r");
	s1 = f1.read();
	f1.close();
	reg1 = re.compile("<tr id=\"section_row\">.*?/tr>", re.MULTILINE | re.DOTALL);
	arr = reg1.findall(s1);
	arrNew = [];
	for ele in arr:
		reg2 = re.compile("<td.*?>(.*?)</td>", re.MULTILINE | re.DOTALL)
		arrTDs = reg2.findall(ele);
		if arrTDs[2] != "&nbsp;":
			arrNew.append(ele);
	return arrNew
print(len(extractCourse()));

arrNew = extractCourse()
def extractMajors(arr):
	arrRet = [];
	for ele in arrNew:
		reg1 = re.compile("<td.*?>(.*?)</td>", re.MULTILINE | re.DOTALL);
		arr = reg1.findall(ele);
		x = arr[2];
		if not(x in arrRet):
			arrRet.append(x);
	return arrRet;
arr2 = extractMajors(arrNew);
print(arr2);
print(len(arr2));

def HofProf(arr):
	profit = 0
	for ele in arrNew:
		reg1 = re.compile("<td.*?>(.*?)</td>", re.MULTILINE | re.DOTALL);
		arr = reg1.findall(ele);
		profit += float(arr[6]) * float(arr[11]) * 1380;
	return profit;
arr3 = HofProf(arrNew);
print(arr3)
print("Dr. Fu is amazing!!!")
