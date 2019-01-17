n = int(input("Enter a number: "));
c = 0
i = 2
z = n - 1
bPrime = True
while  i*i <=n:
	if n%i == 0:
		c = c + 1;
		bPrime = False
		break
	i = i + 1;
print(str(bPrime) + " " +  str(c));
