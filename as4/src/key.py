n = 60001;
bFound = False
while bFound == False:
	Prime = True
	i = 2
	while i*i  <= n:
		if n%i == 0:
			Prime = False
			break;
		i = i + 1
	if Prime == True:
		bFound = True;
	else: 
		n = n + 1			
print(n); 
