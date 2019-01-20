from random import choice
import itertools
Defect = 0
Cooperate = 1
class Agent:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.history = {} # a dict, key is another agent, value is a list of events where self interacted with another agent
        self.totalscore = 0
    def choice(self,opponent):
        if opponent in self.history:
            hist = self.history[opponent]
        else: hist = []
        pick = self.strategy(hist)
        return pick
    def recordhist(self,opponent,oppPlay,reward):
        if opponent not in self.history:
            self.history[opponent] = []
        self.history[opponent].append(oppPlay)
        self.totalscore += reward
    def gettotalscore(self):
        return self.totalscore

def confront(a1,a2):
    a1choice = a1.choice(a2)
    a2choice = a2.choice(a1)
    if a1choice == a2choice:
        if a1choice == Defect:
            a1reward = 1
            a2reward = 1
        else:
            a1reward = 3
            a2reward = 3
    else:
        if a1choice == Defect:
            a1reward = 5
            a2reward = 0
        else:
            a1reward = 0
            a2reward = 5
    a1.recordhist(a2,a2choice,a1reward)
    a2.recordhist(a1,a1choice,a2reward)

def AllD(history):
    return Defect

def AllC(history):
    return Cooperate

def TFT(history):
    if len(history) == 0:
        return Cooperate
    else:
        return history[-1]

#Cooperate Unitl Other Defects
def Grudge(history):
    for x in history:
        if x == Defect:
            return Defect
    return Cooperate
    
#Alternate between Cooperating and Defecting
def CthenD(history):
    if len(history)%2==0:
        return Cooperate
    else: return Defect

#Alternate between Defecting and Cooperating
def DthenC(history):
    if len(history)%2==0:
        return Defect
    else: return Cooperate
    
#Cooperates 50% of the time until opponent defects then defects all the time
def fiftyfiftyC(history):
    for x in history:
        if x == Defect:
            return Defect
        else:
            return choice([Defect,Cooperate])
        
#Cooperates all of the time until opponent defects then defects 50% of the time        
def fiftyfiftyD(history):
    for x in history:
        if x == Defect:
            return choice([Defect,Cooperate])
        else:
            return Cooperate
        
        
#Cooperates all of the time until opponent defects then defects 2/3 of the time 
def TwoThirdD(history):
    for x in history:
        if x == Defect:
            return choice([Defect,Defect,Cooperate])
        else:
            return Cooperate

#Cooperates 2/3 of the time until opponent defects then defects all the time
def TwoThirdC(history):
    for x in history:
        if x == Defect:
            return Defect
        else:
            return choice([Defect,Cooperate,Cooperate])
        
#Always Cooperates turn one then after that has a 66% chance of defecting       
def Defect66(history):
    if len(history) == 0:
        return Cooperate
    else:
        return choice([Defect,Defect,Cooperate])

def Random(history):
    return choice([Cooperate,Defect])
    
#new code that creates my contenders list by going through a list and appending the items to the list of contenders instead of appending each one one by one
strategies = [AllD,AllC,TFT,Grudge,CthenD,fiftyfiftyD,TwoThirdD,Defect66,Random]

strategydict = {AllD:"AllD",AllC:"AllC",TFT:"TFT",Grudge:"Grudge",CthenD:"CthenD",fiftyfiftyD:"50-50D",TwoThirdD:"2/3D",Defect66:"Defect66%",Random:"Random"}

contenders = []
for strategy in strategies:
    contenders.append(Agent(strategydict[strategy],strategy))

def printscores():
    for x in contenders:
        print("The score of " + x.name + " = " + str(x.gettotalscore()))

rounds = int(input("Enter how many rounds you would like to play. Max rounds is 300. "))

for round in range(rounds):
    #new code to delete one strategy after every 50 rounds and then add a copy of each of the strategies remaining and reset scores to zero
    if round>0 and round%50==0:
        loser = contenders[0].strategy
        minscore = contenders[0].gettotalscore()
        for c in contenders:
            score = c.gettotalscore()
            if score < minscore:
                loser = c.strategy
                minscore = c.gettotalscore()
        for i in range(len(contenders)):
                    if contenders[i].strategy == loser:
                        deleteidx = i
        del(contenders[deleteidx])
        print(strategydict[loser])
        for strategy in strategies:
            if strategy == loser:
                strategies.remove(strategy)
        contenders = []
        for event in range(int(round/50)+1):
            for strategy in strategies:
                contenders.append(Agent(strategydict[strategy],strategy))
    for x in itertools.combinations(contenders,2):
        confront(x[0],x[1])
    

printscores()

