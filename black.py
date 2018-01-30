def box(n,x,a): #Test Name, Function(variable inputs), What should be returned
        return (x==a)

def boxIntRange(n,min,max,x):# Test Name, Minimim(inclusive), Maximim(inclusive), actual
	return ((x >= min) and (x <= max))#if returned within range expected

def boxM(n,x,a): #Test Name, Function(variable inputs), What should be returned
	return (x in a)
def p(n):
        print("%s: Passed"% n)#print pass
def f(n,x,a):
        print("%s: Failed - expected: \"%s\", recived : \"%s\""% (n,a,x))
