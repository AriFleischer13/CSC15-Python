iNumber = int(input("How many textbooks are you buying? "));
bookprice = 132.24;
if iNumber>=1 and iNumber<=10: print("Final Price = "+ str((bookprice*iNumber)*.98))
elif iNumber>=11 and iNumber<=20: print("Final Price = "+ str((bookprice*iNumber)*.95))
elif iNumber>=21 and iNumber<=100: print("Final Price = "+ str((bookprice*iNumber)*.90))
elif iNumber>100: print("Final Price = "+ str((bookprice*iNumber)*.80))
