import black
def TimesPass(a,b):
        return a*b

def TimesFail(a,b):
        return a+b
	
black.box("TimePass1",TimesPass(10,10),100) # 10*10 should == 100

black.box("TimeFail1",TimesFail(2,2),4) # 2*2 should == 4 (False Negative)
black.box("TimesFail2",TimesFail(10,10),100)
print()
input("Press Ender To Close")
