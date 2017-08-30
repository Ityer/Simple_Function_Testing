def box(n,x,a): #Test Name, Function(variable inputs), What should be returned
	if x == a: #if returned is as expected
		return True
	else:
		f(n,x,a)#print fail
		return False

def boxIntRange(n,min,max,x):# Test Name, Minimim(inclusive), Maximim(inclusive), actual
	if (x >= min) and (x <= max):#if returned within range expected
		print("%s: Passed"% n)#print pass
		return True
	else:
		f(n,x,("Between %s and %s"%(min,max)))#print fail
		return False

def boxM(n,x,a): #Test Name, Function(variable inputs), What should be returned
	if x in a: #if returned is as expected
		print("%s: Passed"% n)#print pass
		return True
	else:
		f(n,x,a)#print fail
		return False
def p(n):
        print("%s: Passed"% n)#print pass
def f(n,x,a):
        print("%s: Failed - expected: \"%s\", recived : \"%s\""% (n,a,x))
