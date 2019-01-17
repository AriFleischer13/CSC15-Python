def readData(filename):
	fStock = open (filename,"r");
	arrLines = fStock.readlines();
	fStock.close();
	x = len(arrLines)-1;
	arrRet = []; 
	while x>0:
		arr2 = arrLines[x].split(",");
		arrNew = [];
		arrNew.append(arr2[0]);
		arrNew.append(float(arr2[1]));
		arrRet.append(arrNew);
		x -= 1;
	return arrRet;
print(readData("GOOG.csv"));

def get10DayAvg(data, i):
	idx = i-1
	sum = 0
	c = 0
	if i ==0:
		return data[0][1]
	else:
		while idx >= 0 and c<10:
			sum += data[idx][1]
			c += 1
			idx = idx - 1	
	avg = sum/c
	return avg
data = readData("GOOG.csv")
avgLast = get10DayAvg(data, len(data)-1);
print("10-day Avg for last day: " + str(avgLast));

def backtest(data, perc, initFund):
	decimal = perc/100.0;
	fCash = initFund;
	iShares = 0;
	for day in range(0,len(data)):
		Avg = get10DayAvg(data,day);
		price = data[day][1];
		if price < (1 - decimal)*Avg:
			iSharesToBuy = int(fCash/data[day][1]);
			fCash = fCash - (data[day][1]*iSharesToBuy);
			iShares = iShares + iSharesToBuy;
		if price > (1 + decimal)*Avg:
			fCash = fCash + (data[day][1]*iShares);
			iShares = 0
	total = fCash + (iShares*data[len(data)-1][1]);
	return total;	
data = readData("GOOG.csv");
initFund = 10000.0;
total = backtest(data, 1.0, initFund);
profit = (total - initFund)/initFund*100.0;
print("profit is " + str(profit) + "%");

perc = 0.1
bestperc = 0
bestvalue = 0 
while perc < 10:
	if bestvalue < backtest(data, perc, initFund):
		bestvalue = backtest(data, perc, initFund);
		bestperc = perc;
	perc = perc + 0.1
profit = (bestvalue - initFund)/initFund*100
print("max profit is " + str(profit) + "%, at perc: " + str(bestperc) + "%");
	
