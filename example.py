import black, random
def TimesPass(a,b):#multiply two inputs and return result - functional
	return a*b

def TimesFail(a,b):#multiply two inputs and return result - non-functional
	return a+b

def RandomOneToTen(min,max):#random number generator
	return random.randint(min,max)

black.box("TimePass1",TimesPass(10,10),100) # 10*10 should == 100

black.box("TimeFail1",TimesFail(2,2),4) # 2*2 should == 4 (False possitive)
black.box("TimesFail2",TimesFail(10,10),100)
print()
black.boxIntRange("RandomOneToTenPass",1,10,random.randint(1,10))
for i in range(10):
        black.boxIntRange("RandomOneToTenFail1",1,10,random.randint(1,15)) #will mostly return as passed

black.boxM("Mpass",5,[1,2,3,4,5])
black.boxM("Mfail",99,[1,2,3,4,5])
input("Press Enter To Close")
