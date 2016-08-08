def box(n,x,a): # Test Name, Function(variable inputs), What should be returned
	if x == a:
		print("%s: Passed"% n)
		return True
	else:
		print("%s: Failed"% n)
		return False

def boxIntRange(n,min,max,a):# Test Name, Minimim(inclusive), Maximim(inclusive), actual
	if (a >= min) and (a <= max):
		print("%s: Passed"% n)
		return True
	else:
		print("%s: Failed"% n)
		return False