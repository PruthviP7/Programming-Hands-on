def MaxMin(no1,no2):
	if(no1 > no2):
		return no1

	else:
		return no2

def CheckDivisible(ino):
	if((ino % 3 == 0) and (ino % 5 == 0)):
		return True
	else:
		return False